print(f"{'='*25}")
print(f"{'Analisador de Palavras':^25}")
print(f"{'='*25}")
palavras = ("Aprender", "Programar", "Linguagem", "Python", "Curso", "Gratis", "Estudar", "Praticar", "Trabalhar", "Mercado", "Programador", "Futuro")
vogal = ()
for word in palavras:
    vogal = ()
    #print("Palavra: ",word) #Palavra
    print(f"\nNa palavra {word.upper()} temos: ", end="")
    for letters in range(len(word)):
        #print("Letras: ",word[letters]) #Letras da Palavra
        if word[letters].lower() in "aeiou":
            vogal = (*vogal, word[letters])
    for v in vogal:
        print(f"{v.lower()}", end=" ")
    del(vogal)