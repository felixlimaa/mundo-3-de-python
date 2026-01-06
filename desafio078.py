valores = []
for i in range(0, 5):
    valores.append(int(input(f"Digite um valor para posição {i}: ")))
#valores = [1, 2, 1, 5, 5]
max = max(valores)
min = min(valores)
print("-=" * 30)    
print(f"Você digitou os valores {valores}", end="")
print(f"\nO maior valor digitado foi {max} nas posições", end="... ")
if max in valores:
    max = [i[0] for i in enumerate(valores) if i[1] == max]
    for i in max:
        print(i, end="... ")
print(f"\nO menor valor digitado foi {min} nas posições", end="... ")
if min in valores:
    min = [i[0] for i in enumerate(valores) if i[1] == min]
    for i in min:
        print(i, end="... ")