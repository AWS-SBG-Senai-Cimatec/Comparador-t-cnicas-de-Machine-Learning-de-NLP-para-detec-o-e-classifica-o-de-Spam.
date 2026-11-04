# Aula 08 - Interface do comparador em Streamlit

Data proposta: 30/11/2026; horário a combinar.

Objetivo: Conectar entrada de mensagem, modelo salvo e tabela de comparação.

## Estudar

- [Streamlit: conceitos básicos](https://docs.streamlit.io/get-started/fundamentals/main-concepts)

## A - Prática isolada

Construir uma tela pequena isolada

1. Crie em exercicios/seu-nome/ uma tela Streamlit com campo de texto, botão e exibição do tamanho.
2. Mostre uma orientação para texto vazio; a tela didática não classifica mensagens.

Conferir:

- A interação funciona e trata vazio; você explica a reexecução do Streamlit.
- O resultado é apenas tamanho de texto, sem uma previsão falsa de modelo.

Guardar a solução em `exercicios/seu-nome/aula-08/`.

## B - Contribuição ao Projeto 04

Entregar a interface funcional e cuidada do Projeto 04

Pré-requisito: Modelos e inferência da aula 07; validação da aula 02.

1. Integrar seleção dos dois modelos, entrada validada e previsão por pipeline salvo.
2. Exibir comparação real de validação, métricas por classe e limites das classes binárias.
3. Aplicar dark mode, roxo, hierarquia legível, logos oficiais e estados claros de erro/carregamento; verificar em notebook e tela estreita.

Arquivos ou artefatos: `app.py; src/predict.py; src/validation.py; docs/uso.md`

Critérios de conclusão:

- [ ] A previsão vem de artefato real; o app não treina a cada clique.
- [ ] Usuário encontra como testar uma mensagem e comparar modelos; sem texto cortado ou resultado inventado.

Ao concluir: Aplicação utilizável com classificação e comparação reais.

## Entrega e revisão

Abrir PR ligado à issue. Conferir critérios, explicar a solução e responder à revisão. Validar A não conclui B automaticamente.

[Voltar à trilha](../aulas.md)
