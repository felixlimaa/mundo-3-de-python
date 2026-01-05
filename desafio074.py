from random import randint
legado = ()
for i in range(5): #4 vezes
    i = randint(1, 100) #gera um número aleatório
    i += 1
    legado = (*legado, i)
print(f"Os valores sorteados foram: ", end="")
for l in legado:
    print(f"{l}", end=" ")
print(f"\nO maior valor sorteado foi: {max(legado)}")
print(f"O menor valor sorteado foi: {min(legado)}")