numeros = []
for i in range(0, 5):
    numeros.append(int(input("Digite um número: "))) #5
    if len(numeros) >= 2: #12
        b = numeros[i] #12
        a = numeros[i-1] #5
        if a > b:
            numeros.remove(a)
            numeros.insert(b, a)
        elif b > a:
            numeros.remove(b)
            numeros.insert(a, b)
        del(b, a)
        if len(numeros) >= 3:
            for j in numeros:
                if j[i] < j[i]
    print(numeros) #[12, 12, 12, 12, 90, 12]