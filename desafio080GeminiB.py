#Treino extra de Insertion Sort (ou Ordenação por Inserção)
nome = []
for i in range(0,5):
    nome.append(str(input(f"Digite o {i+1}º nome: ").strip()))
    p = len(nome) - 1
    while p > 0 and nome[p] < nome[p-1]:
        temp = nome[p]
        nome[p] = nome[p-1]
        nome[p-1] = temp
        print(f"{nome[p]} adicionado na posição {p}.")
        print(f"{nome[p-1]} adicionado na posição {p-1}.")
        p = p - 1
    print(f"Nomes em ordem alfabética: {nome}")