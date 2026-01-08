valores = ordem = []
c = ""
while True:
    valores.append(int(input("Digite um número: ")))
    for i, v in enumerate(valores): #nao repete  valor inserido dentro da lista
        if v in valores and valores.count(v) > 1:
            print("Número já está na lista, não vou adicionar...")
            valores.pop(i)
    c = str(input("Você quer adicionar mais algum número? [S/N]: ")).strip().upper()[0]
    while c not in "NS":
        c = str(input("Você quer adicionar mais algum número? [S/N]: ")).strip().upper()[0]
    if "N" in c:
        break
print(f"Você digitou os números: ", end=" ")
for v in valores:
    print(v, end=" ")
ordem = sorted(valores, reverse=False)
print(f"\nOrdem crescente dos números: ", end=" ")
for o in ordem:
    print(o, end=" ")
print("\nPrograma encerrado")