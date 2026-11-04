# Aula 06 - Primeiro classificador de mensagens

Data proposta: 23/11/2026; horário a combinar.

Objetivo: Treinar uma referência simples e um pipeline textual em conjunto.

## Estudar

- [scikit-learn: classificação de texto](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)
- [scikit-learn: divisão e vazamento](https://scikit-learn.org/stable/common_pitfalls.html)

## A - Prática isolada

Observar texto virando vetor e previsão

1. Use seis mensagens fictícias curtas, divididas em duas classes didáticas, em um exemplo acompanhado.
2. Ajuste TF-IDF apenas no treino fictício, observe os termos e gere uma previsão de demonstração.

Conferir:

- O vetor representa termos do treino; a previsão vem de um modelo ajustado.
- Resultados da base fictícia não são apresentados como desempenho do Projeto 04.

Guardar a solução em `exercicios/seu-nome/aula-06/`.

## B - Contribuição ao Projeto 04

Entregar o primeiro caminho de treino do comparador

Pré-requisito: Split da aula 05 aprovado; exemplos fictícios separados dos dados reais.

1. Consumir as divisões reais aprovadas, sem acessar o teste.
2. Treinar DummyClassifier e Pipeline TF-IDF + MultinomialNB.
3. Gerar métricas de validação por classe, macro-F1, matriz de confusão e tempo; analisar erros.

Arquivos ou artefatos: `src/train.py; src/evaluate.py; reports/validacao-baseline.json; reports/validacao-nb.json`

Critérios de conclusão:

- [ ] O treino e a avaliação podem ser executados por comando documentado.
- [ ] Relatórios identificam execução, divisão, classes e parâmetros; cada pessoa explica um erro.

Ao concluir: Baseline e primeiro modelo reais treináveis e avaliáveis.

## Entrega e revisão

Abrir PR ligado à issue. Conferir critérios, explicar a solução e responder à revisão. Validar A não conclui B automaticamente.

[Voltar à trilha](../aulas.md)
