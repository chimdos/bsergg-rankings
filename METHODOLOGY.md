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
Entretanto, não existe apenas uma cabeça super pensante, mas sim várias, e mesmo que uma opinião conjunta possa ser mais válida que o sistema de pontos oficial, a percepção visual errônea da maioria, mesmo que da minioria dos especialistas, pode enviesar a classificação final.
Esse sistema se mostra ótimo para uma noção geral, mas peca em dizer com maior precisão a ordem dos times, especialmente quando chegamos na faixa dos dez melhores de cada região.

1.1.3. E isso nos leva para mais um modelo melhor que o anterior, o ranking matemático da BSEN. 