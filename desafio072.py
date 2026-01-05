números = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
o = ""
while True:
    n = int(input("Digite um número entre 0 e 20: "))
    while n < 0 or n > 20:
        n = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    print(f"Você digitou o número {números[n]}.")
    o = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while o not in "NS":
        o = str(input("Opção inválida. Quer continuar? [S/N]: ")).strip().upper()[0]
    if o in "NS":
        if o == "N":
            break
print("Programa encerrado. Volte sempre!")