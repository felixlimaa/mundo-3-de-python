def tio(simbolo,numero):
    print(simbolo*numero)

def escreva(texto):
    tam = len(texto)+2
    tio('~', tam)
    print(' '*(tam//len(texto)), end="")
    print(texto, end="")
    print(' '*(tam//len(texto)))
    tio('~', tam)

escreva(f'Gustavo Guanabara!')
escreva(f'Curso de Python no YouTube')
escreva(f'CeV')