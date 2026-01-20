from random import randint
from time import sleep
def somaPar(numeros):
    print(f"Somando os valores pares de {numeros}, temos", end=" ", flush=True)
    pares = [p for p in numeros if p % 2 == 0]
    print(f"{sum(pares)}.", flush=True)
def sorteia():
    sleep(0.5)
    print(f"Sorteando 5 valores da lista: ", flush=True)
    numeros = [randint(0,50) for n in range(5)]
    for n in numeros:
        print(n, end=" ", flush=True)
        sleep(0.5)
    print("PRONTO!", flush=True)
    somaPar(numeros)
sorteia()