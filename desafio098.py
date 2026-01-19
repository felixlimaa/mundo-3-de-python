from random import randint
from time import sleep
def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}:")
    while inicio <= fim:
        print(inicio, end=" ")
        inicio = inicio + passo
        sleep(1)
contador(1, 10, 1)