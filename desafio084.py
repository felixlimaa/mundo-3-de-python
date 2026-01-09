pessoas = []
temp = []
continuar = ""
while True:
    temp.append(str(input("Nome: ").strip().lower().capitalize()))
    temp.append(int(input(f"Peso: ")))
    pessoas.append(temp[:])
    temp.clear()
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if continuar in "N":
        break
nome = [n[0] for n in pessoas]
peso = [i[1] for i in pessoas]
pesoLeve = [i for i in pessoas if i[1] <= 70]
pesoPesado = [i for i in pessoas if i[1] >= 100]
print(f"Pessoas cadastradas: {len(pessoas)}")
print(f"As pessoas menos pesadas foram {[i[0] for i in pesoLeve]} com {[i[1] for i in pesoLeve]}.")
print(f"As pessoas mais pesadas foram {[i[0] for i in pesoPesado]} com {[i[1] for i in pesoPesado]}.")