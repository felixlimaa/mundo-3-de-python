pessoas = []
temp = []
maior = 0
menor = 0
continuar = ""
while True:
    temp.append(str(input("Nome: ").strip().lower().capitalize()))
    temp.append(float(input(f"Peso: ")))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if continuar in "N":
        break
print(f"Pessoas cadastradas: {len(pessoas)}")
print(f"O maior peso foi de {maior}. Peso de ",end="")
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end=" ")
print()
print(f"O menor peso for de {menor}. Peso de ",end=" ")
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]",end=" ")
print()