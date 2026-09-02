<h1 align="left">BSERgg Team Rankings</h1>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0--alpha.1-orange" alt="Version 1.0.0-alpha.1" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python 3.11" />
  <img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg" alt="GPL GNU v3" />
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status Active" />
</p>

<img src="assets/BSERgg full logo.png" />

A public Brawl Stars team ranking model designed to measure the current competitive strength accurately.

_This version is still in Alpha for accuracy validation in external environments. Help us by sending feedback on [Twitter](https://x.com/chimdosBS)._

### Current Top 10 – August 31st, 2026
| P | TEAM | REGION | POINTS |
| :---: | :--- | :---: | :---: |
| 1 | FUT Esports | EMEA | 1320 |
| 2 | HMBLE | EMEA | 1241 |
| 3 | ZETA DIVISION | East Asia | 1034 |
| 4 | Crazy Raccoon | East Asia | 896 |
| 5 | Tribe Gaming | North America | 885 |
| 6 | Team Elektros | North America | 713 |
| 7 | Bounty Hunters | South America | 568 |
| 8 | Reply Totem | EMEA | 444 |
| 9 | Vatic Esports | North America | 437 |
| 10 | LOUD | South America | 420 |

_[See the full list here](rankings.md)_

---

## Table of Contents

<details>
<summary>Click to expand</summary>

1. [Getting Started](#getting-started)
2. [Deep Dive & Architecture](#deep-dive--architecture)
3. [Project Governance](#project-governance)

</details>

---

## Getting Started

Setting up the project requires a few steps to prepare your local environment.

### Prerequisites

* Python 3.11
* A local environment (venv)

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/chimdos/bsergg-rankings.git
    cd bsergg-rankings
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    winget install Python.Python.3.11
    ```

### Usage Examples

After setting up your virtual environment and installing Python (if you don't have it installed already), running the main script evaluates the data and generates the rankings. Execute this interpreter directly from your terminal.

  ```bash
  python engine/tournament_interpreter.py
  ```

---

## Deep Dive & Architecture

The system relies on a mathematical framework to evaluate competitive play fairly.

### Features

* Calculates performance points for individual players based on match yields.
* Evaluates entire tournament brackets to assign objective scores.
* Applies a half-life decay formula to older events to favor recent form.
* Merges player scores to formulate an aggregate team standing.

### Tech Stack

The entire application runs exclusively on Python.

### Configuration

The core engine maintains backward compability and works reliably on Python 3.7 and newer releases

---

## Project Governance

We welcome community input to improve mathematical models and codebase.

### Contributing

Detailed contribution guidelines are available in this repository header tab. You can also read the full rules in our [Contributing Guide](CONTRIBUTING.md).

### License

This software is distributed under the GNU General Public License v.3.0. Please refer to the [LICENSE](LICENSE) file for complete terms.

### Community & Support

If you have questions about the math or need help navigating the code, reachout directly to [@chimdosBS](https://x.com/chimdosBS) on Twitter/X.
