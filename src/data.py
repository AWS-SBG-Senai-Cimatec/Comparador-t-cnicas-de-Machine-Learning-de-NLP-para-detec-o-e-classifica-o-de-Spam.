from validation import validar_mensagem, padronizacao

cTexto = "Texto: "
cRotulo = "Rotulo: "
Coluna = (cTexto, cRotulo)

cValidacao = (0,1)

def conferirC(nome):
    """se espera como entrada uma lista com o nome(s) da(s) coluna(s)"""
    cEncontrado = set(nome)
    for coluna in Coluna:
        if coluna not in cEncontrado:
            return coluna

def padronizarTexto(valor):
    resultVal = validar_mensagem(valor)
    if not resultVal.valida:
        raise ValueError("Coluna Vazia: ", cTexto)
    return resultVal.texto

def padronizarRotulo(valor):
    rot = padronizacao(valor)
    if rot not in ("0","1"):
        raise ValueError ("")
    return int(rot)

def padronizarCsv(valor):
    faltante = conferirC(valor.keys())
    if faltante:
        raise ValueError("Não está presente colunas obrigatorias: ",faltante)
    return print(cTexto, padronizarTexto(valor[cTexto]),"\n",cRotulo, padronizarRotulo(valor[cRotulo]))
