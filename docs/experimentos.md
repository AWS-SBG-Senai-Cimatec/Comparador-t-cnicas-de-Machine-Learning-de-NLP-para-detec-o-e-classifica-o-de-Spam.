# Protocolo dos experimentos

Proposta: treino/validação/teste 60/20/20, adaptada a grupos e contagens por classe. Fixar IDs, seed e versão dos dados. Ajustar TF-IDF somente no treino. Comparar baseline, Naive Bayes e regressão logística no mesmo protocolo.

Escolher configuração por validação; teste reservado para avaliação após congelamento. Registrar macro-F1, métricas por classe, matriz de confusão, tempo de treino e erros.

Metadados: run_id, commit do treino, hash dos dados, parâmetros, seed, versões de dependências e métricas. Salvar Pipeline completa com Joblib e verificar igualdade de previsões ao recarregar.
