temp = [] #poderia ser [[0, 0, 0], [0, 0, 0], [0, 0, 0]] também.
n = [] #Se usasse o de cima da maneira não usada, não precisaria dessa declaração.
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