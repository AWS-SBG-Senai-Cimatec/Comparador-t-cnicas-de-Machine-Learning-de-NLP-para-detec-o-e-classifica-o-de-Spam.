# Aula 03 - Funções, listas e laços

Data proposta: 12/11/2026; horário a combinar.

Objetivo: Criar uma função reutilizável e aplicá-la a uma lista de mensagens.

## Estudar

- [Python: condições e laços](https://www.cursoemvideo.com/curso/python-3-mundo-2/)
- [Python: funções e controle de fluxo](https://docs.python.org/pt-br/3/tutorial/controlflow.html)
- [GitHub: primeiro PR](https://docs.github.com/pt/get-started/using-github/hello-world)

## A - Prática isolada

Reutilizar uma função em uma lista

1. Crie analisar_mensagem(texto) retornando válida, tamanho e contém_urgente.
2. Aplique à lista [" Ola ", "URGENTE", "   "]; preveja a saída antes de executar.

Conferir:

- Tamanhos: 3, 7 e 0; só o segundo contém urgente; o terceiro é inválido.
- Você explica parâmetro, laço, dicionário e retorno.

Guardar a solução em `exercicios/seu-nome/aula-03/`.

## B - Contribuição ao Projeto 04

Definir funções e contrato dos dados do projeto

Pré-requisito: Validação da aula 02 e inspeção do esquema com André.

1. Definir funções pequenas para conferir colunas obrigatórias e padronizar a leitura de texto/rótulo.
2. Documentar o contrato real: text_combined e label, rótulos binários; não alterar seus significados.
3. Revisar a função de validação com um colega e demonstrar uma entrada diferente.

Arquivos ou artefatos: `src/data.py; docs/dados.md; src/validation.py`

Critérios de conclusão:

- [ ] As funções têm entrada/saída documentadas; não há três cópias de lógica em src/.
- [ ] O contrato lista os campos que serão lidos na aula 04, com dúvidas de dados registradas.

Ao concluir: Contrato de dados e funções básicas preparados para leitura do CSV.

## Entrega e revisão

Abrir PR ligado à issue. Conferir critérios, explicar a solução e responder à revisão. Validar A não conclui B automaticamente.

[Voltar à trilha](../aulas.md)
