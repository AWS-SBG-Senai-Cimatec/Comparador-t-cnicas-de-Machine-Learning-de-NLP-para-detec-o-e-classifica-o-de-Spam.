# Aula 04 - CSV, pandas e qualidade dos dados

Data proposta: 16/11/2026; horário a combinar.

Objetivo: Ler uma tabela e descrever o que existe antes de treinar modelos.

## Estudar

- [pandas: leitura e resumo de tabelas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [Dataset do projeto](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset)

## A - Prática isolada

Inspecionar uma tabela fictícia

1. Leia data/exemplos/mensagens_didaticas.csv e conte linhas, classes e ausências.
2. Entre textos não vazios, conte repetições além da primeira com strip/lower.

Conferir:

- 6 linhas, classes legitima=3/phishing=3, 1 texto vazio e 1 repetição.
- Essa tabela é apenas didática e fica fora das métricas do comparador.

Guardar a solução em `exercicios/seu-nome/aula-04/`.

## B - Contribuição ao Projeto 04

Implementar leitura e qualidade da base real

Pré-requisito: Contrato da aula 03 e obtenção autorizada da base.

1. Implementar a leitura do agregado phishing_email.csv e validar o contrato de colunas.
2. Contar classes, vazios, duplicatas e conflitos de rótulo; registrar decisões antes de limpar.
3. Excluir vazio e tratar duplicatas/grupos conforme decisão registrada; guardar IDs e proveniência.

Arquivos ou artefatos: `src/data.py; docs/dados.md; reports/qualidade-dados.json`

Critérios de conclusão:

- [ ] Antes da limpeza: 82.486 linhas, classes 0=39.595 e 1=42.891; 1 vazio e 408 repetições por strip/lower.
- [ ] Há relatório de contagens antes/depois e decisão sobre conflitos; o CSV real não entra no Git.

Ao concluir: Leitura e preparação dos dados reais funcionando e documentadas.

## Entrega e revisão

Abrir PR ligado à issue. Conferir critérios, explicar a solução e responder à revisão. Validar A não conclui B automaticamente.

[Voltar à trilha](../aulas.md)
