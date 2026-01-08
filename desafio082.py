n = par = impar = []
continuar = ""
while True:
    n.append(int(input("Digite um número: ")))
    par = [i for i in n if i % 2 == 0]
    impar = [i for i in n if i % 2 != 0]
    continuar = str(input("Continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Continuar? [S/N]: ")).strip().upper()[0]
    if continuar in "N":
        break
print(f"Números digitados: {n}")
print(f"Pares digitados: {par}")
print(f"Ímpares digitados: {impar}")
print("Programa encerrado!")