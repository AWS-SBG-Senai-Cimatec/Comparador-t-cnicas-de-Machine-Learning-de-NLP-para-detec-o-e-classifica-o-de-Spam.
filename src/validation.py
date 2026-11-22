import math
from dataclasses import dataclass

texto_vazio = "Digite uma mensagem para continuar."

@dataclass(frozen=True)
class resultVal:
    validacao: bool
    texto: str
    orientacao: str

def padronizacao(texto):
    if texto is None:
        return ""
    if isinstance(texto, float) and math.isnan(texto):
        return ""
    return str(texto).strip()

def validar_mensagem(texto):
    mensagem = padronizacao(texto)
    if mensagem == "":
        return resultVal(validacao=False, texto="", orientacao=texto_vazio)
    return resultVal(validacao=True, texto=mensagem, orientacao="")
