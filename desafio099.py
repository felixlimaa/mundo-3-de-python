from random import randint
from time import sleep
def maior(* numeros):
    top = m = 0
    for n in numeros:
        if n > top:
            top = m
    print(f"Foram gerados {len(numeros)} números.")
    print(f"O maior número digitado foi {m}.")
legado = ()
contador = (5, 3, 2, 1, 0)
grupo = []
for f in range(len(contador)):    
    for g in range(contador[f]):
        g = randint(0, 10)
        g += 1
        legado = (*legado, g)
        print(legado, flush=True)
        grupo.append(legado)
        del legado
        
        sleep(0.25)