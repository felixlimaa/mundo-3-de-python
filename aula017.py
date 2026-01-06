a = [2, 3, 4, 7]
b = a[:] #Cria uma cópia de 'a' em 'b'
b[2] = 8 #Alteração refletida em 'a' também
print(f"A lista A é {a}") #A lista A é [2, 3, 4, 7]
print(f"A lista B é {b}") #A lista B é [2, 3, 8, 7]

"""
valores = list()
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))


for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
"""
"""
num = [2, 5 , 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
#num.pop() #remove o último elemento
#num.pop(2) #remove o elemento da posição 2
#num.remove(2) #remove o primeiro valor 2 encontrado
if 5 in num: 
    num.remove(4)
else:
    print("Não achei o número 4")
print(num)
print(f"Essa lista tem {len(num)} elementos.")"""