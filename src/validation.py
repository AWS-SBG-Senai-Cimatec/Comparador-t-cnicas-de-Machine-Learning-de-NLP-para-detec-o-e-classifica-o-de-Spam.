class resultVal:
      validacao: bool
      texto: str

def validar_mensagem(texto):
    if texto is None:
        texto = ""

    mensagem = texto.strip()

    if mensagem == "":
         return resultVal(validacao = False, texto = "")
    return resultVal(validcao = True, texto=mensagem)
