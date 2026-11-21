# Aula 02 - Analise de texto no terminal

## Objetivo
Criar um script para receber texto e ver a quantidade, utilize a função strip() para tirar qualquer espaçamento desnecessario 
e ver se contem a mensagem urgente, usando a função lower() para ler mesmo se for tudo maiusculo

mens contem a mensagem, tamanho usa a função lens() para contar o tamanho e urg é o questionamento para ver se apareceu essa mensagem

    def analise(mensagem):
        mens = mensagem.strip()
        if mens == "": 
            return None
        tamanho = len(mensagem)
        urg = "urgente" in mensagem.lower()
        return mens, tamanho, urg

    def main():
       digitacao = input("Digite a mensagem: ")
       result = analise(digitacao)

    if result is None:
       print("Esqueceu de escrever")
       return 

    mens, tamanho, urg = result
    print("Mensagem: ", mens)
    print("Tamanho: ", tamanho)
    print("Tem urgente? : ", urg)

    main()
    
