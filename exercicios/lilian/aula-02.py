# 1. Crie um script isolado que receba texto, aplique strip() e mostre o tamanho.
# 2. Verifique se contém urgente sem diferenciar maiúsculas e recuse a entrada vazia.

def meu_script():
    texto = input("Escreva seu texto: ")
    
    texto_branco = texto.strip()
    
    if not texto_branco:
        print("Entrada vazia não é permitida!")
        return None
    
    texto_indiferenciavel = texto_branco.lower()
    
    print(f"Texto original: {texto}")
    print(f"Texto sem espaço: {texto_branco}")
    print(f"Tamanho do texto: {len(texto_indiferenciavel)}")
    print(f"Texto indiferenciável: {texto}")
    
    return texto_indiferenciavel

if __name__ == "__main__":
    meu_script()