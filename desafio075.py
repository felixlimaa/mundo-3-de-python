legado = pares = ()
for i in range(4):
    i = int(input("Digite um valor: "))
    legado = (*legado, i)
for p in legado:
    if p % 2 == 0:
        pares = (*pares, p)
    p += 1
print(f"Você digitou os valores {legado}")
if 9 not in legado:
    print("O número 9 não foi digitado em nenhuma posição.")
else:
    print(f"O número 9 apareceu {legado.count(9)} vezes.")
if 3 not in legado:
    print("O número 3 não foi digitado em nenhuma posição.")
else:
    print(f"O primeiro número 3 apareceu na posição {legado.index(3)}.") #7 primeiro #10 segundo
print(f"Números pares: ", end="")
for p in pares:
    print(f"{p} ", end="")