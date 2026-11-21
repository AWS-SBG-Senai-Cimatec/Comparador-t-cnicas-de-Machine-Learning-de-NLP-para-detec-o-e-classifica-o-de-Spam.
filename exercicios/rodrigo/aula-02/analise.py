def analise(mensagem):
    mens = mensagem.strip()
    if mens == "":
        return None
    tamanho = len(mens)
    urg = "urgente" in mens.lower()
    return mens, tamanho, urg


def main():
    digitacao = input("Digite a mensagem: ")
    result = analise(digitacao)
    if result is None:
        print("Esqueceu de escrever")
        return
    mens, tamanho, urg = result
    print("Mensagem limpa:", mens)
    print("Tamanho:", tamanho)
    print("Contém 'urgente':", urg)


if __name__ == "__main__":
    main()
