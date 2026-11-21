## Aula 02 - Analisar texto no terminal

# Objetivo
Ler mensagem, limpar texto desnecessario, contar a quantidade de palavras e ver se tem urgente ou não

## Funções
- lens() - retorna o numero de objetos
- strip() - remove espaçamento em branco

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
      print(f"Mensagem limpa: ", mens)
      print(f"Tamanho: ", tamanho)
      print(f"Contém 'urgente': ", urg)

      main()
    
