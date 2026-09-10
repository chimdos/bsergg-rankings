<!-- 

1. Problema e solução inicial - ausência de ranking de lógica pública, necessidade de transparência e desafio para medir com precisão o momento ATUAL do cenário de esports
2. Como diferenciar as forças de diferentes regiões
3. Como saber quais torneios pesam mais no circuito BSC de 2026
4. Como o tempo afeta os torneios
5. Como a rostermania é resolvida e o problema do substituto
6. Como pesar vitórias e derrotas baseado no placar (yields)
6.1. O que acontece se a partida não for uma Bo5

WIP: Como pesar forças diferentes de times em yields diferentes

-->

1. É possível dizer com certeza qual é a posição de cada time entre os melhores do mundo?
A resposta curta é: não, é impossível medir com total precisão. Por isso, esse projeto se fundamenta na necessidade da existência de um modelo matemático que possa atingir uma assertividade satisfatória.

1.1. Mas e os outros rankings?
Hoje, temos a classificação oficial do BSC, a opinião da comunidade e dos especialistas, e o ranking matemático da BSEN. Entretanto, esses três sofrem de problemas que limitam sua melhor acurácia hipotética.

1.1.1. A classificação regional do BSC serve para apenas um propósito, decidir quem se classifica para os eventos internacionais. Ela funciona como um cartão fidelidade, premiando a regularidade de quem chega mais longe nos circuitos mensais, mas falha em medir uma dominância real dentro do jogo.
Pense no seguinte cenário: o Time A vence uma Final Mensal atropelando todos os adversários por 3 a 0. No mês seguinte, o Time B é campeão, mas ganhando todas as suas partidas de 3 a 2. Para o ranking oficial, ambos os times recebem a mesma quantidade de pontos. Além disso, a classificação também não combina os pontos das regiões de forma ponderada, e algumas sub-regiões tem circuitos diferentes das quatro regiões principais.
Ou seja, a tabela oficial não importa como você venceu, apenas se você venceu, o que é excelente para organizar campeonatos, mas é um medidor falho se quisermos descobrir qual time é mais forte e eficiente no momento.

1.1.2. Isso nos leva para o próximo melhor modelo, a opinião pública. A opinião de especialistas e da comunidade é mais assertiva que a classificação do BSC porque uma cabeça pensante sabe a diferença entre ganhar um título atropelando todos de 3 a 0 e ganhar sofridamente todos os jogos de 3 a 2. Além disso, uma cabeça pensante também entende melhor a recência dos eventos, e que o momento atual é mais importante que a longevidade de pontos.
Entretanto, não existe apenas uma cabeça super pensante, mas sim várias, e mesmo que uma opinião conjunta possa ser mais válida que o sistema de pontos oficial, a percepção visual errônea da maioria, mesmo que da minioria dos especialistas, pode enviesar a classificação final. Além disso, uma pessoa europeia tende a valorizar mais a Europa, assim como uma norte-americana tende a valorizar mais a América do Norte, e assim por diante, isso causa um viés e favoritismo regional. Outra coisa é a falta de memória estatística; o cérebro humano é influenciado pela extrema recência, uma pessoa pode facilmente colocar um time que ganhou um torneio ontem no topo da tabela, esquecendo que o mesmo time teve um desempenho terrível um ou dois meses atrás, algo que, mesmo nosso próprio modelo BSERgg valorizando bastante, pondera bem melhor que um ser biológico pensante. 
Esse sistema se mostra ótimo para uma noção geral, mas peca em dizer com maior precisão a ordem dos times, especialmente quando chegamos na faixa dos dez melhores de cada região.

1.1.3. E isso nos leva para mais um modelo melhor que o anterior, o ranking matemático da BSEN. O modelo da BSEN é o primeiro passo real para um modelo computacional de sucesso, entretanto, o mesmo sofre de amostra pequena, pois não coloca as classificatórias mensais do BSC na conta, e também não considera a força dos confrontos de cada time ao longo do torneio, tornando uma avaliação matemática mais precisa difícil. Além disso, o ranking da BSEN não tem sua lógica pública, algo que tira a confiança do algoritmo e impossibilita a comunidade de contribuir e melhorar o motor de cálculo.

1.2. Então como medir algo com a melhor precisão possível?
Para isso, é necessário pesar as forças de diferentes regiões, quantificar quais torneios tem mais peso que outros, entender como o tempo afeta o peso de um resultado num torneio, entender como resultados por partida importam num torneio e pesá-los, e entender como resultados contra times de diferentes forças pesam na pontuação final.

2. Como diferenciar as forças das diferentes regiões
Desempenho histórico e recente em torneios internacionais, infraestrutura financeira e quantidade de organizações profissionais, ecossistema de base e comparação de força adaptativa em cadeia.

A força de uma região dita o quão boa ela é no jogo, mas ela não é uniforme, e por isso é dividida em chão e teto.
Primeiro, é preciso analisar o desempenho histórico e a quantidade de vagas em eventos internacionais.
Análise estatística dos resultados das regiões
Vagas por região nas World Finals (2019–2026)
Nº de vagas
Categoria	EMEA	América do Norte	América do Sul	Leste Asiático	China	SESA
2019	2	1	1	2	0	1
2021	6	2	2	2	3	1
2022	6	3	3	2	1	1
2023	5	3	1	1	1	1
2024	5	3	2	2	0	0
2025	7	3	2	1	0	1
2026	4	2	2	2	0	0

Títulos
EMEA 3
Leste Asiático 3

Ao olhar pra isso, vemos que a EMEA e a East Asia são claramente as regiões de maior destaque. Entretanto, é necessário analisá-las também pela perspectiva de chão e teto.
Ambas regiões possuem hoje 3 títulos mundiais, e considerando torneios de meio de temporada, a EMEA fica com mais 2 e a East Asia com mais 1. Além disso, historicamente, a distribuição de times classificados pelo LCQ (que existe desde 2023) é:
Categoria	EMEA	América do Norte	América do Sul	Leste Asiático	China	SESA
2023	2	1	0	0	0	1
2024	2	1	1	0	0	0
2025	2	0	0	1	0	1
Total   6   2   1   1   0   1

Ou seja, a EMEA possui um teto levemente maior que a East Asia e possui maior chão/profundidade que a mesma, colocando-a como região mais forte, assim vindo logo em seguida a East Asia.

Dando continuidade, precisamos olhar para as regiões sem título internacional, portanto devemos olhar aos Top 4 de cada Mundial até hoje:
Categoria	EMEA	América do Norte	América do Sul	Leste Asiático	China	SESA
2019	1	1	0	2	0	0
2021	2	0	1	1	0	0
2022	0	2	0	2	0	0
2023	2	1	0	1	0	0
2024	3	0	0	1	0	0
2025	2	0	0	1	0	1
Total   10  4   1   8   0   1

Podemos ver que a próxima região na lista de força é claramente a North America, mas que fica bem atrás do que a EMEA e da East Asia, sendo apenas 1 dos 4 top 4s um vice-campeonato.

Depois disso entramos num impasse entre South America e SESA, a South America apresentou até hoje mais times competindo em campeonatos internacionais, mas continua empatada com a SESA tanto na quantidade de times classificados pelo LCQ até hoje e pela quantidade de aparições no top 4 dos Mundiais. Entretanto, ao olharmos detalhadamente para os resultados, perceberemos que as conquistas da SESA dependem pesadamente da lineup da Revenant, podendo ser considerada até uma one-team region, o que coloca a South America consideravelmente acima em chão/profunidade, apesar da proximidade em teto.

A análise dos resultados mais recentes também favorece mais a EMEA em detrimento a East Asia, já que a final da Brawl Cup foi entre dois times da EMEA. A mesma East Asia também sofreu no Challengers Istanbul, e não conseguiu passar os dois times da sua região para os playoffs, enquanto a EMEA, além de passar 4 dos seus 5 times disputando, contemplou 3 times da região no top 4, uma final totalmente europeia e portanto um campeão também europeu.