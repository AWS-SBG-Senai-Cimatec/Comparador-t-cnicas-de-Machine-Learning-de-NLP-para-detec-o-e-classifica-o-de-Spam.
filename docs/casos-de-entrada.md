# Casos de entrada - Interface do usuário

A função validar_mensagem(texto) em src/validation.py é usado como validação para ver se a mensagem contém algo ou não.
Utiliza uma classe, contendo apenas um booleano para validação e a mensagem.

### Validação
True - A mensagem tem algum conteudo nela.

False - A mensagem é vazia

### Exemplos

"" - Mensagem vazia, não envia para validação

" " - Mensagem vazia, não envia para validação

None - Campo sem valor, não enviar para validação

" Ola " - Conteudo encontrado, envia para validação

"Urgente" - Conteudo encontrado, envia para validação

"Qualquer texto" - Conteudo encontrado, envia para validação 
