Este repositório vai contemplar tanto a coleta de dados das APIs da RIOT quanto a análise dos dados e aplicação das técnicas de machine learning.

# Objetivo

Coletar dados de partidas de todos tiers (ferro, bronze, prata, ouro, platina, diamante, mestre, grandmaster e challenger) e aplicar algoritmos de clusterização para observar se é possível classificar corretamente uma partida ao seu tier correspondente.

# Estratégia de coleta de dados

A API da Riot não possui um end point para retornar todos os nomes de jogadores de um tier, portanto precisamos de uma estratégia de primeiramente encontrar um player de um elo específico. Este será nossa 'semente' e a partir dele o código coleta players aos quais jogaram com o player_semente.

Assim, de posse de uma lista de players, é possível coletar o código de identificação da partida e a partir dela, acessar as estatísticas dos times.

# Coleta de dados

## Definição das classes

Para a coleta dos dados da API da Riot não foi utilizado a biblioteca já implementada. Como parte do aprendizado, o código foi desenvolvido para coletar as informações que precisávamos. 

O arquivo _RiotConsts.py_ possui a formatação do link das apis, e o arquivo _riotApi.py_ as definições das classes que serão utilizadas ao longo do código da coleta de dados.

O _riotApi.py_ posui 4 classes (até o momento): 

_(mais classes podem ser adicioanadas ao longo do projeto)_

**- GetSummoner():** será utilizada para solicitar dados do summoner, a partir do nome de usuário.

**- Getmatchlist():** será utilizada para solicitar uma lista de partidas, a partir do accountID do summoner.

**- GetmatchStats():** será utilizada para solicitar métricas de uma determinada partida, a partir do gameID da partida.

**- GetmatchPerChamp():** será utilizada para retornar uma lista de partidas em função de alguns filtros, com por exemplo um determinado champion.


No arquivo _fluxograma.pdf_ você pode visualizar mais detalhes da estratégia de coleta adotada.