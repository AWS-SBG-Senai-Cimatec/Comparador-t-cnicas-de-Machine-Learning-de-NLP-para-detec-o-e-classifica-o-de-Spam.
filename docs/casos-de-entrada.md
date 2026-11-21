# Casos de Entrada

Documentação com o intuito de descrever o passo a passo para a execução do script que analisa mensagens suspeitas, bem como os casos de teste para validação do funcionamento da função 'analise()'.

## 1. Como executar o código

1. Certifique-se de ter o Python instalado em sua máquina.
2. Abra o terminal (ou prompt de comando).
3. Navegue até a pasta 'src/validation.py'.
4. Execute o comando no terminal aberto:

   ```bash
   python validation.py

## 2. Casos de teste

O código foi desenvolvido para remover espaços em branco extras, contar a quantidade de caracteres e verificar se a palavra "urgente" está presente, sem que haja distinção de maiúscula.

### Caso SEM 'urgente'

1. ENTRADA(INPUT): "Olá, tudo bem? Vamos marcar a reunião para amanhã."
2. SAÍDA (OUTPUT):
    Mensagem limpa: Olá, tudo bem? Vamos marcar a reunião para amanhã.
    Tamanho: 48
    Contém 'urgente': False

### Caso COM 'urgente'

1. ENTRADA(INPUT): "Olá, tudo bem? Vamos marcar a reunião para amanhã."
2. SAÍDA (OUTPUT):
    Mensagem limpa: URGENTE! Você ganhou um prêmio, clique no link.
    Tamanho: 47
    Contém 'urgente': True

### Caso com entrada vazia

1. ENTRADA(INPUT): "  " (Usuário não digita)
2. SAÍDA (OUTPUT): Esqueceu de escrever

### Caso de mensagem com espaços extras nas bordas

1. ENTRADA(INPUT): " Preciso de ajuda "
2. SAÍDA (OUTPUT):
    Mensagem limpa: Preciso de ajuda
    Tamanho: 16
    Contém 'urgente': False