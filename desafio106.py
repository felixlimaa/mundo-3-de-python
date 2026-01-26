from cores import design
def titulo(texto="", simbolo='s'):
    corTexto = 'branco'
    fundo = 'fundo verde'
    print(design(simbolo*(len(texto)+4), c=corTexto, b=fundo))
    print(design(f'  {texto}  ', c=corTexto, b=fundo))
    print(design(simbolo*(len(texto)+4), c=corTexto, b=fundo))
def ajuda(texto):
    h = help(texto)
    return h
while True:
    titulo('SISTEMA DE AJUDA PyHELP', '~')
    info = str(input("Função ou Biblioteca > ")).strip()
    ajuda(info)
    
