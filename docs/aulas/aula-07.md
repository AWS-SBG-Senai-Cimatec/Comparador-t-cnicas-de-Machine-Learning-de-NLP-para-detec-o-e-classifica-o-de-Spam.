# Aula 07 - Comparação, métricas e Joblib

Data proposta: 26/11/2026; horário a combinar.

Objetivo: Comparar dois modelos de forma justa e recarregar os pipelines salvos.

## Estudar

- [scikit-learn: classificação de texto](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)
- [Persistência dos modelos](https://scikit-learn.org/stable/model_persistence.html)

## A - Prática isolada

Entender métricas e persistência

1. Com TP=3, FP=1 e FN=2, calcule precisão, recall e F1 no papel e confira com Python.
2. Salve e recarregue um pequeno dicionário criado por você com Joblib; explique o que foi preservado.

Conferir:

- Precisão=0,75; recall=0,60; F1≈0,667.
- O dicionário recarregado coincide com o original; isso não versiona sozinho um experimento.

Guardar a solução em `exercicios/seu-nome/aula-07/`.

## B - Contribuição ao Projeto 04

Completar a comparação e os modelos recarregáveis

Pré-requisito: Primeiro modelo e relatórios da aula 06; sem ajustar escolhas pelo teste.

1. Adicionar regressão logística no mesmo split e na mesma configuração textual inicial.
2. Gerar comparação dos modelos e baseline; selecionar pela validação e justificar os erros relevantes.
3. Salvar pipelines completos e metadados; recarregar e comparar previsões antes/depois em três textos.

Arquivos ou artefatos: `src/train.py; src/evaluate.py; src/predict.py; reports/comparacao_validacao.csv; models/<run_id>/`

Critérios de conclusão:

- [ ] As configurações usam o mesmo protocolo e a tabela é gerada por código.
- [ ] Previsões antes/depois coincidem; metadados registram commit, dados, versões e parâmetros.

Ao concluir: Comparador de modelos completo, com persistência e inferência reutilizável.

## Entrega e revisão

Abrir PR ligado à issue. Conferir critérios, explicar a solução e responder à revisão. Validar A não conclui B automaticamente.

[Voltar à trilha](../aulas.md)
