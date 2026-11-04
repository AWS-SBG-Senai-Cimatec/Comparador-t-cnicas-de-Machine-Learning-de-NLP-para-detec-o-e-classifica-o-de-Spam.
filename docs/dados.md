# Contrato e qualidade dos dados

Fonte: https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset

Arquivo agregado: phishing_email.csv, versão 1, inspecionado em 04/11/2026. 82.486 linhas; colunas text_combined e label. Rótulos: 0 = 39.595; 1 = 42.891. A descrição do publicador associa essas contagens a legítimos e spam, agrupando spam/phishing. Não há rótulo independente para distinguir spam de phishing.

Qualidade inicial: 1 texto vazio; 408 repetições além da primeira entre textos não vazios normalizados por strip/lower. Revisar conflitos de rótulo, templates e origem antes da divisão.

Licença informada pelo publicador: CC BY-SA 4.0. Registrar atribuição e fonte. Hash SHA-256 do CSV: 73a5c5410baf46ed69517fedfd37910f2e93777dc504b73ea483bc16be3a69d1. Tamanho: 106.603.543 bytes.

Usar o agregado isoladamente, sem concatená-lo às bases de origem. Dados reais ficam em data/raw fora do Git; dados/exemplos é fictício, apenas para prática. Em T07/T09, confirmar idioma, revisar exemplos e proveniência e documentar limpeza e split.
