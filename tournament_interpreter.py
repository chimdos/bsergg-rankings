import re
import json
import math
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
from collections import defaultdict


# --- DATA MODELS ---

@dataclass(frozen=True)
class TeamStanding:
    team_name: str
    region: str
    points: float


# --- CONSTANTS & CONFIGURATION ---

REGIONAL_FORCE_MULTIPLIERS: Dict[str, float] = {
    "International": 1.00,
    "EMEA": 1.00,
    "East Asia": 0.85,
    "Japan": 0.85,
    "Italy": 0.85,
    "North America": 0.75,
    "DACH": 0.70,
    "South America": 0.60,
    "Brazil": 0.60,
    "Spain": 0.60,
    "Turkey": 0.60,
    "France": 0.55,
    "SESA": 0.45,
    "Southeast Asia": 0.45,
    "South Asia": 0.45,
    "China": 0.30,
    "South America West": 0.20,
    "Korea": 0.15,
}

EVENT_TIERS = {
    "brawl_cup_2026": {"half_life": 60, "base_points": {"1": 800, "2": 550, "3-4": 400, "5-8": 250, "9-12": 120, "13-16": 60}},
    "world_finals_2026": {"half_life": 100, "base_points": {"1": 1000, "2": 700, "3-4": 500, "5-8": 300, "9-12": 150}},
    "lcq_2026": {"half_life": 60, "base_points": {"1": 400, "2": 300, "3-4": 200, "5-8": 100}},
    "monthly_finals": {"half_life": 60, "base_points": {"1": 150, "2": 110, "3-4": 80, "5-8": 55}},
    "monthly_qualifier": {"half_life": 60, "base_points": {"1-4": 45, "5-8": 30, "9-12": 20, "13-16": 15, "17-24": 8, "25-32": 3}},
    "sesa_2026_rtbc": {"half_life": 60, "base_points": {"1": 300, "2": 220, "3": 160, "4": 120, "5-6": 75}},
    "southamericawest_2026_rtbc": {"half_life": 60, "base_points": {"1": 450, "2": 330, "3": 240, "4": 180, "5-8": 100, "9-12": 50}},
    "complementary": {"half_life": 60, "base_points": {"1": 90, "2": 65, "3-4": 45, "3": 45, "4": 30, "5-6": 20, "5-8": 20, "7-8": 10, "9-12": 10, "13-16": 5}}
}

YIELD_MATRIX: Dict[str, Dict[Tuple[int, int], float]] = {
    "bo3": {(2, 0): 1.00, (2, 1): 0.70, (1, 2): 0.30, (0, 2): 0.00},
    "bo5": {(3, 0): 1.00, (3, 1): 0.85, (3, 2): 0.70, (2, 3): 0.30, (1, 3): 0.15, (0, 3): 0.00},
    "bo7": {(4, 0): 1.00, (4, 1): 0.88, (4, 2): 0.75, (4, 3): 0.60, (3, 4): 0.40, (2, 4): 0.25, (1, 4): 0.12, (0, 4): 0.00},
}


# --- CORE LOGIC ---

class RegionTracker:
    def __init__(self) -> None:
        self._team_region_counts: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))

    def process_event_for_regions(self, event_data: dict) -> None:
        region = event_data.get("region", "International")
        
        if region == "International":
            return

        rosters = event_data.get("rosters", {})
        for team_name in rosters.keys():
            self._team_region_counts[team_name][region] += 1

    def get_region(self, team_name: str) -> str:
        if team_name not in self._team_region_counts or not self._team_region_counts[team_name]:
            return "International"
        
        region_counts = self._team_region_counts[team_name]
        most_frequent_region = max(region_counts, key=region_counts.get)
        
        return most_frequent_region


class MathEngine:
    @staticmethod
    def calculate_decay(event_date_str: str, target_date: datetime, half_life_days: int) -> float:
        event_date = datetime.strptime(event_date_str, "%Y-%m-%d")
        days_elapsed = max(0, (target_date - event_date).days)
        return math.pow(0.5, days_elapsed / half_life_days)

    @staticmethod
    def get_match_yield(score_a: int, score_b: int, format_type: str) -> Tuple[float, float]:
        matrix = YIELD_MATRIX.get(format_type.lower(), YIELD_MATRIX["bo5"])
        
        default_a = 1.00 if score_a > score_b else 0.00
        default_b = 1.00 if score_b > score_a else 0.00
        
        yield_a = matrix.get((score_a, score_b), default_a)
        yield_b = matrix.get((score_b, score_a), default_b)
        
        return yield_a, yield_b


class TournamentScorer:
    def __init__(self, target_date: datetime):
        self.target_date = target_date

    def score_tournament(self, event_data: dict) -> Dict[str, float]:
        player_points: Dict[str, float] = defaultdict(float)
        
        config = self._get_event_config(event_data.get("event_type", ""))
        rfm = REGIONAL_FORCE_MULTIPLIERS.get(event_data.get("region", ""), 1.00)
        decay = MathEngine.calculate_decay(event_data.get("date", "2026-01-01"), self.target_date, config["half_life"])
        
        team_yields = self._calculate_average_yields(event_data.get("matches", []))
        
        placements = event_data.get("placements", {})
        rosters = event_data.get("rosters", {})
        
        for placement_key, teams in placements.items():
            base_points = self._resolve_base_points(config["base_points"], placement_key)
            
            for team in teams:
                avg_yield = team_yields.get(team, 1.00)
                team_earned_points = base_points * avg_yield * rfm * decay
                
                team_roster = rosters.get(team, [])
                self._distribute_points_to_players(team_roster, team_earned_points, player_points)
                
        return dict(player_points)

    def _distribute_points_to_players(self, roster: List[str], team_points: float, global_player_points: Dict[str, float]) -> None:
        for raw_player_name in roster:
            is_sub = bool(re.search(r'\(sub\)', raw_player_name, re.IGNORECASE))
            clean_name = re.sub(r'\(sub\)', '', raw_player_name, flags=re.IGNORECASE).strip()
            
            multiplier = 0.5 if is_sub else 1.0
            global_player_points[clean_name] += team_points * multiplier

    def _get_event_config(self, event_type: str) -> dict:
        if event_type in EVENT_TIERS:
            return EVENT_TIERS[event_type]
        if "challengers" in event_type or "regional" in event_type:
            return EVENT_TIERS["complementary"]
        return EVENT_TIERS["monthly_finals"]

    def _resolve_base_points(self, base_points_dict: dict, placement: str) -> float:
        if placement in base_points_dict:
            return float(base_points_dict[placement])
            
        for key, points in base_points_dict.items():
            if "-" in key and self._is_in_range(placement, key):
                return float(points)
        return 0.0

    def _is_in_range(self, placement: str, range_key: str) -> bool:
        if not placement.isdigit():
            return False
        low, high = map(int, range_key.split("-"))
        return low <= int(placement) <= high

    def _calculate_average_yields(self, matches: list) -> Dict[str, float]:
        yields_accum: Dict[str, List[float]] = {}
        
        for match in matches:
            team_a = match.get("team_a")
            team_b = match.get("team_b")
            score_a = int(match.get("score_a", 0))
            score_b = int(match.get("score_b", 0))
            fmt = match.get("format", "bo5")
            
            y_a, y_b = MathEngine.get_match_yield(score_a, score_b, fmt)
            
            if team_a: yields_accum.setdefault(team_a, []).append(y_a)
            if team_b: yields_accum.setdefault(team_b, []).append(y_b)
            
        return {team: sum(y) / len(y) for team, y in yields_accum.items() if y}


# --- INFRASTRUCTURE & EXPORT ---

class JsonRepository:
    def load_all_tournaments(self, directory_path: str) -> List[dict]:
        tournaments = []
        path = Path(directory_path)
        
        for json_file in path.rglob("*.json"):
            if "template" in json_file.name.lower() or "teams" in json_file.name.lower():
                continue
                
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "event_type" in data:
                        tournaments.append(data)
            except Exception as e:
                print(f"Failed to read {json_file.name}: {e}")
                
        return tournaments

    def load_active_teams(self, filepath: str) -> Dict[str, List[str]]:
        path = Path(filepath)
        if not path.exists():
            print(f"Warning: Active teams file not found at {filepath}")
            return {}
            
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("teams", {})
        except Exception as e:
            print(f"Failed to read active teams: {e}")
            return {}


class MarkdownExporter:
    def export_standings(self, standings: List[TeamStanding], output_filepath: str) -> None:
        markdown_content = self._format_standings_to_markdown(standings)
        self._write_to_file(markdown_content, output_filepath)

    def _format_standings_to_markdown(self, standings: List[TeamStanding]) -> str:
        lines = [
            "# Global BSERgg Rankings",
            "",
            "| POSITION | TEAM NAME | REGION | TOTAL POINTS |",
            "| :---: | :--- | :---: | :---: |"
        ]
        
        for index, standing in enumerate(standings, start=1):
            safe_team_name = standing.team_name.replace('|', r'\|')
            lines.append(
                f"| {index} | **{safe_team_name}** | {standing.region} | {standing.points:.2f} |"
            )
            
        return "\n".join(lines)

    def _write_to_file(self, content: str, filepath: str) -> None:
        output_path = Path(filepath)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(content)
            
        print(f"Ranking exportado com sucesso em: {output_path.name}")


# --- ORCHESTRATION ---

class LeaderboardOrchestrator:
    def __init__(self, target_date: datetime, current_teams: Dict[str, List[str]]):
        self.target_date = target_date
        self.current_teams = current_teams
        self.region_tracker = RegionTracker()
        self.scorer = TournamentScorer(target_date)

    def generate_global_standings(self, tournaments: List[dict]) -> List[TeamStanding]:
        global_player_points: Dict[str, float] = defaultdict(float)

        for tournament in tournaments:
            self.region_tracker.process_event_for_regions(tournament)
            
            event_player_scores = self.scorer.score_tournament(tournament)
            for player_name, points in event_player_scores.items():
                global_player_points[player_name] += points

        standings = []
        for team_name, roster in self.current_teams.items():
            team_points = sum(global_player_points.get(player, 0.0) for player in roster)
            region = self.region_tracker.get_region(team_name)
            
            standings.append(TeamStanding(
                team_name=team_name,
                region=region,
                points=team_points
            ))
        
        return sorted(standings, key=lambda s: s.points, reverse=True)


if __name__ == "__main__":
    DATA_DIRECTORY = "./tournaments"
    CURRENT_TEAMS_FILE = "./tournaments/current_teams.json"
    OUTPUT_FILE = "rankings.md"
    EVALUATION_DATE = datetime(2026, 8, 30)

    repository = JsonRepository()
    tournaments_data = repository.load_all_tournaments(DATA_DIRECTORY)
    current_teams_dict = repository.load_active_teams(CURRENT_TEAMS_FILE)

    if tournaments_data and current_teams_dict:
        orchestrator = LeaderboardOrchestrator(EVALUATION_DATE, current_teams_dict)
        final_standings = orchestrator.generate_global_standings(tournaments_data)

        exporter = MarkdownExporter()
        exporter.export_standings(final_standings, OUTPUT_FILE)
    else:
        print("Error: No valid tournament nor current teams file found.")