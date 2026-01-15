estudante = {}
#dicionário['palavra'] = explicação --> números e/ou palavras
estudante['nome'] = str(input("Nome: ")).strip().capitalize()
estudante['média'] = float(input(f"Média de {estudante["nome"]}: "))
if estudante['média'] >= 7:
    estudante['situação'] = "aprovado"
else:
    estudante['situação'] = "desaprovado"
print(estudante)
for d, s in estudante.items(): #[d]icionário [s]ignificado
    print(f"{d.capitalize()} é igual a {s}.")