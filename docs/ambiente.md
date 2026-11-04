# Preparar o ambiente

Usar Python 3.12 e Git. As dependências foram instaladas e conferidas em Windows com Python 3.12; as versões diretas estão em `requirements.txt` e o conjunto resolvido está em `requirements.lock.txt`.

## Windows / PowerShell

Dentro da pasta clonada:

```powershell
python --version
git --version
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.lock.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -c "import pandas, sklearn, joblib, streamlit; print('Ambiente pronto')"
```

Invocar o Python da `.venv` evita depender da ativação no PowerShell. Se o comando `python` não estiver disponível, verificar a instalação com André antes de alterar configurações do sistema.

## Linux / macOS

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.lock.txt
.venv/bin/python -m pip check
.venv/bin/python -c "import pandas, sklearn, joblib, streamlit; print('Ambiente pronto')"
```

Os comandos acima para Linux/macOS ainda precisam ser conferidos em uma máquina da equipe com esse sistema. Se alguma dependência não tiver distribuição compatível, registrar o erro na issue de ambiente em vez de alterar versões sem combinar.

## Dados e execução do projeto

O exemplo fictício está em `data/exemplos/mensagens_didaticas.csv`. A base real deve ser obtida da [fonte indicada](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset), conforme [docs/dados.md](dados.md), e guardada em `data/raw/`.

Treino, avaliação e interface serão implementados nas tarefas das aulas. Seus comandos devem ser acrescentados ao README assim que existirem. Não há aplicativo ou modelo pronto nesta etapa de organização.
