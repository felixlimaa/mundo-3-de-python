exp = str(input("Digite uma expressão: ").strip()) #((8*2)-10)
pAbertos = len([p for p in exp if "(" in p])
pFechados = len([p for p in exp if ")" in p])
print(f"Parênteses abertos: {pAbertos}")
print(f"Parênteses fechados {pFechados}")
if pAbertos == pFechados:
    print(f"A expressão {exp} é válida.")
else:
    print(f"A expressão {exp} é inválida.")