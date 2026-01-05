lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata Frita")
print(lanche) #("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata Frita")
print(lanche[1]) #Suco
print(lanche[-2]) #Pizza
print(lanche[1:3]) #('Suco', 'Pizza')
print(lanche[2:]) #('Suco', 'Pizza', 'Pudim')
print(lanche[:2]) #('Hambúrguer', 'Suco')
print(lanche[-2:]) #('Pizza', 'Pudim')
print(len(lanche[-3:])) #3

#Tuplas são imutáveis
#lanche[1] = "Refrigerante" #Gera um erro

for comida in lanche:
    print(f"Eu vou comer {comida}")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print("Comi pra caramba!")

print(sorted(lanche)) #['Batata Frita', 'Hambúrguer', 'Pizza', 'Pudim', 'Suco']

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a) #(2, 5, 4)
print(b) #(5, 8, 1, 2)
print(c) #(2, 5, 4, 5, 8, 1, 2)
print(len(c)) #7
print(c.count(5)) #2
print(c.index(8)) #4
print(c.index(4)) #2
print(c.index(2)) #0
print(c.index(5,1)) #3

pessoa = ("Gustavo", 39, "M", 99.88)
print(pessoa) #('Gustavo', 39, 'M', 99.88)
del(pessoa) #imutabilidade removida
del(pessoa[0]) #Gera um erro, só remove a tupla inteira
# print(pessoa) #Gera um erro