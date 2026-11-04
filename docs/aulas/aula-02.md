# Aula 02 - Python: texto, valores e condições

Data proposta: 09/11/2026; horário a combinar.

Objetivo: Ler uma mensagem, limpar espaços e decidir se a entrada é válida.

## Estudar

- [Python: fundamentos](https://www.cursoemvideo.com/curso/python-3-mundo-1/)
- [Python: funções e controle de fluxo](https://docs.python.org/pt-br/3/tutorial/controlflow.html)

## A - Prática isolada

Analisar texto no terminal

1. Crie um script isolado que receba texto, aplique strip() e mostre o tamanho.
2. Verifique se contém urgente sem diferenciar maiúsculas e recuse a entrada vazia.

Conferir:

- "  Ola  " tem tamanho 3; "URGENTE" tem tamanho 7 e indicador verdadeiro.
- "   " é inválida; a regra não serve para afirmar que uma mensagem é phishing.

Guardar a solução em `exercicios/seu-nome/aula-02/`.

## B - Contribuição ao Projeto 04

Criar a validação de entrada da futura interface

Pré-requisito: Estrutura da aula 01 integrada.

1. Integrar validar_mensagem(texto) com resultado claro para texto válido e vazio.
2. Documentar os casos de entrada e como a interface deve orientar o usuário.
3. Remover do código integrado qualquer regra didática que classifique por palavras como urgente.

Arquivos ou artefatos: `src/validation.py; docs/casos-de-entrada.md`

Critérios de conclusão:

- [ ] Texto só com espaços é rejeitado com orientação; texto válido é preservado para inferência.
- [ ] A validação não inventa uma classificação; terá um único ponto de uso no app.

Ao concluir: Validação reutilizável pronta para a tela de mensagens.

## Entrega e revisão

Abrir PR ligado à issue. Conferir critérios, explicar a solução e responder à revisão. Validar A não conclui B automaticamente.

[Voltar à trilha](../aulas.md)
