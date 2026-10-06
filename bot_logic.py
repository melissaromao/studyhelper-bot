temas = {}
def estudos_temas(tema, status, conteudo):
    temas[tema] = {
    'status': status,
    'conteudo': conteudo
    }
def mostrar_temas():
    return temas