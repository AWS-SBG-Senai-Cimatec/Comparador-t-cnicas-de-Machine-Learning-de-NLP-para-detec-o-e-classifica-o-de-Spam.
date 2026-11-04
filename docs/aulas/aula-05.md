# Aula 05 - Treino, validação e teste

Data proposta: 19/11/2026; horário a combinar.

Objetivo: Separar aprendizado, escolha do modelo e avaliação final sem vazamento.

## Estudar

- [scikit-learn: divisão e vazamento](https://scikit-learn.org/stable/common_pitfalls.html)

## A - Prática isolada

Separar exemplos de estudo e avaliação

1. Separe dez IDs fictícios em treino/validação/teste e explique o papel de cada grupo.
2. Acrescente duas mensagens iguais com IDs diferentes e decida onde elas devem ficar.

Conferir:

- Não há IDs compartilhados; textos equivalentes também não cruzam os grupos.
- Você explica por que escolher parâmetros olhando o teste invalida a avaliação final.

Guardar a solução em `exercicios/seu-nome/aula-05/`.

## B - Contribuição ao Projeto 04

Gerar as divisões reproduzíveis do dataset

Pré-requisito: Dados preparados na aula 04; André valida o protocolo.

1. Gerar split com seed e IDs, usando grupos quando houver correlação; proposta inicial 60/20/20.
2. Conferir contagem por classe, interseção de IDs e de textos equivalentes.
3. Reservar o teste final; versionar configuração e metadados permitidos, mantendo textos/derivados fora do Git.

Arquivos ou artefatos: `src/split.py; configs/experimento.json; docs/experimentos.md; manifesto de IDs`

Critérios de conclusão:

- [ ] Reexecutar gera as mesmas divisões no ambiente e versão de dados registrados.
- [ ] TF-IDF será ajustado só no treino; validação serve à escolha, teste fica reservado.

Ao concluir: Treino, validação e teste definidos para todos os modelos.

## Entrega e revisão

Abrir PR ligado à issue. Conferir critérios, explicar a solução e responder à revisão. Validar A não conclui B automaticamente.

[Voltar à trilha](../aulas.md)
