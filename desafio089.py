temp = []
notas = []
alunos = []
continuar = ""
while True:
    temp.append(str(input("Nome: ")).strip().capitalize())
    notas.append(int(input("Nota 1: ")))
    notas.append(int(input("Nota 2: ")))
    temp.append(notas[:])
    notas.clear()
    media = sum(temp[1])/len(temp[1])
    temp.append(media)
    alunos.append(temp[:])
    temp.clear()
    #print(alunos) #[['Marcos', [6, 9], 7.5], ['Felix', [7, 9], 8.0]]
    continuar = str(input("Quer adicionar mais um aluno? [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Quer adicionar mais um aluno? [S/N]: ")).strip().upper()[0]
    if continuar in "N":
        break
print("Programa encerrado!")