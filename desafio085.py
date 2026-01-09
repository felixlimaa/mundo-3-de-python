n = [[], []]
temp = []
for i in range(0,7):
    temp.append(int(input(f"Digite o {i+1}º número: ")))
    if temp[i] % 2 == 0:
        n[0].append(temp[i])
        n[0].sort()
    else:
        n[1].append(temp[i])
        n[1].sort()
temp.clear()
print(n)
print(f"Os valores pares digitados foram: {n[0]}")
print(f"Os valores ímpares digitados foram: {n[1]}")