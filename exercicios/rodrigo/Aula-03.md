# Atividade A - Aula 03

    def analisar_mensagem(texto):
        mens = texto.strip()
        val = True
        if mens == "": val = False
        elif mens is None: val = False
        tamanho = len(mens)
        urg = "urgente" in mens.lower()
        return print("Mensagem Valida? : ",val,"\nTamanho: ",tamanho,"\ntem Urgente? :",urg)


    mensagem = [" Ola ", "Urgente", " "]

    for conversa in mensagem:
        result = analisar_mensagem(conversa)

## Objetivo
Criar uma função de leitura de mensagems, retornando a validação da mensagem, o tamanho dela e se contém urgente.

Utiliza uma lista para colocar as palavras e um loop for para ler cada mensagem
