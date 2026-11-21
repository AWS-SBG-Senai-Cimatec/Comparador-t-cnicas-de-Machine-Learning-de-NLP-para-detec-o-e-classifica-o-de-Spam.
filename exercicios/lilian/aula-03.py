# Crie analisar_mensagem(texto) retornando válida, tamanho e contém_urgente.
# Aplique à lista [" Ola ", "URGENTE", " "]; preveja a saída antes de executar.

def analisar_mensagem(texto):
    texto_branco = texto.strip()
    tamanho_texto = len(texto_branco)
    texto_valido = tamanho_texto > 0
    contem_urgente = "urgente" in texto_branco.lower()
    
    return {
        "valida": texto_valido,
        "tamanho": tamanho_texto,
        "contem_urgente": contem_urgente, 
    }
    
def main():
    mensagens = [" Ola ", "URGENTE", " "]
    for mensagem in mensagens:
        resultado = analisar_mensagem(mensagem)
        print(f"Entrada: {mensagens} ---> {resultado}")

if __name__ == "__main__":
    main()