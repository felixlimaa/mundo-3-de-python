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
        print(f"[ {n[i][j]} ]", end=" ")
        if j == 2:
            print()