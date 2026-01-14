temp = []
n = []
for i in range(0,3):
    for j in range(0,3):
        temp.append(int(input(f"Digite um valor para {[i, j]}: ")))
        if j == 2:
            n.append(temp[:])
            temp.clear()
for i in range(0,3):
    for j in range(0,3):
        print(f"[ {n[i][j]:^5} ]", end=" ")
        if j == 2:
            print()
pares = [j for p in n for j in p if j%2 == 0]
pares = sum(pares)
colunaDois = [p[2] for p in n]
colunaDois = sum(colunaDois)
print(f"A soma dos valores pares é {pares}.")
print(f"A soma dos valores da terceira coluna é {colunaDois}.")
print(f"O maior valor da segunda linha é {max(n[1])}.")