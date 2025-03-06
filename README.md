# Projeto de Automação com Bot

Este projeto visa automatizar diversas tarefas utilizando um bot. Abaixo está a estrutura de pastas e arquivos do projeto.

## Estrutura de Pastas

- **imagens**: Esta pasta contém as imagens tiradas pelo bot.
- **RequestsDB**: Esta pasta contém os arquivos que puxam a requisição da base de dados.
- **SCRIPTS**: Esta pasta contém os scripts de teste do sistema.
- **WebServices**: Esta pasta conterá o futuro sistema de inserção de usuários do bot.

## Arquivos

- **Datas.py**: Responsável por importar as datas.
- **DetectCondition.py**: Futuro detector de condição.
- **Executar**: Script que roda os passos do bot.
- **getmouseposition.py**: Script que pega a posição atual do mouse.

## Como usar

1. Sete as variaveis de local. A classe 'acao' funciona com base numa serie de funcoes que movem o mouse o fazem clicar nas
coordenadas configuradas manualmente. Futuramente pretendo trocar essa ideia por um insertor de coordenadas.
Tendo em vista que esse é um projeto inicial a inserção das posições seram feitas de forma manual.

2. Execute o código. Ele faz todos os passos (menos ler o QRCode) de forma automatica para a geração do AD.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues no tópico.