# Construção incremental do Projeto 04

Cada aula tem duas entregas: A, exercício isolado de compreensão; B, contribuição revisada que integra o comparador. A solução A fica em exercicios/<nome>/; a contribuição B vai para src/, app.py, docs/ ou relatórios, conforme a etapa. O projeto integrado tem uma única implementação por função, construída em conjunto e revisada.

As datas do calendário são propostas; a entrega final acordada é 07/12/2026. O encerramento depende do funcionamento dos critérios abaixo, não apenas do término das aulas. Este documento define entregas a implementar; não afirma que o software já foi construído.

| Aula | A - Compreender | B - Acrescentar ao projeto | Estado ao concluir |
| --- | --- | --- | --- |
| 01 | Praticar branch, commit e PR | Preparar a base de colaboração do comparador | Repositório organizado, com primeiro fluxo de contribuição funcionando. |
| 02 | Analisar texto no terminal | Criar a validação de entrada da futura interface | Validação reutilizável pronta para a tela de mensagens. |
| 03 | Reutilizar uma função em uma lista | Definir funções e contrato dos dados do projeto | Contrato de dados e funções básicas preparados para leitura do CSV. |
| 04 | Inspecionar uma tabela fictícia | Implementar leitura e qualidade da base real | Leitura e preparação dos dados reais funcionando e documentadas. |
| 05 | Separar exemplos de estudo e avaliação | Gerar as divisões reproduzíveis do dataset | Treino, validação e teste definidos para todos os modelos. |
| 06 | Observar texto virando vetor e previsão | Entregar o primeiro caminho de treino do comparador | Baseline e primeiro modelo reais treináveis e avaliáveis. |
| 07 | Entender métricas e persistência | Completar a comparação e os modelos recarregáveis | Comparador de modelos completo, com persistência e inferência reutilizável. |
| 08 | Construir uma tela pequena isolada | Entregar a interface funcional e cuidada do Projeto 04 | Aplicação utilizável com classificação e comparação reais. |
| 09 | Revisar instruções com outra pessoa | Validar a entrega candidata e sua qualidade visual | Versão candidata reproduzida, demonstrável e revisada. |
| 10 | Explicar uma contribuição com clareza | Entregar o Projeto 04 final funcionando | Projeto 04 pronto para demonstração e uso educacional, com entrega identificada. |

## Definição de pronto

- [ ] Uma pessoa consegue preparar o ambiente, obter a base permitida e executar o treino seguindo o README.
- [ ] A qualidade e o esquema dos dados, a origem, a licença e as classes binárias estão documentados.
- [ ] Dois classificadores e uma baseline usam o mesmo protocolo sem vazamento; o teste final é reservado até congelar escolhas.
- [ ] Tabela comparativa, métricas por classe, macro-F1, tempos e matrizes são gerados por código e identificam a divisão.
- [ ] Pipelines completos são salvos com Joblib e recarregados com previsões consistentes; há metadados de execução.
- [ ] O app permite escolher modelo, digitar mensagem, obter previsão e consultar a comparação real.
- [ ] A interface tem dark mode, roxo, logos oficiais, boa hierarquia e leitura; foi verificada em notebook e tela estreita.
- [ ] Vazio, modelo ausente e outros erros previstos recebem orientações; o app não treina a cada clique.
- [ ] Não há resultados inventados, promessas de acerto garantido nem afirmação de separar spam e phishing sem rótulos adequados.
- [ ] Código revisado, instruções, proposta AWS e apresentação estão entregues; cada pessoa explica uma contribuição.

## Revisão e responsabilidade

Todos fazem A individualmente. Em B, uma pessoa integra a contribuição, outra revisa e as demais participam por pareamento e casos de verificação; alternar papéis. O Tech Lead confere critérios, desbloqueia e valida a integração. Dificuldade individual gera apoio, não uma tarefa marcada como concluída sem entendimento.
