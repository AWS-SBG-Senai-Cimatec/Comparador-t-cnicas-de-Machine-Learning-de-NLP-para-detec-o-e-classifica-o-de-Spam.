import os

msg = ""
while True:
    msg = input("Digite uma mensagem: ")
    msg = msg.strip()
    msg = msg.lower()
    if "urgente" in msg:
        urgente = True
    else:
        urgente = False

    

    if msg == "":
        os.system("cls")
        print("Mensagem vazia, tente novamente!")
        
    else:
        print(f"Mensagem: {msg} | Tamanho: {len(msg)} | Urgente: {urgente}")
        break