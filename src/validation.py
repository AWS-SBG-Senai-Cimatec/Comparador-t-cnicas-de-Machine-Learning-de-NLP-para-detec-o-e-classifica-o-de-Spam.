from dataclasses import dataclass

texto_vazio = "Digite uma mensagem para continuar."


@dataclass(frozen=True)
class resultVal:
    validacao: bool
    texto: str
    orientacao: str


def validar_mensagem(texto):
    """Valida str ou None, removendo espaços nas pontas, sem classificar o texto."""
    if texto is None:
        texto = ""

    mensagem = texto.strip()

    if mensagem == "":
        return resultVal(validacao=False, texto="", orientacao=texto_vazio)
    return resultVal(validacao=True, texto=mensagem, orientacao="")
