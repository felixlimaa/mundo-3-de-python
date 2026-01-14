from random import randint
from time import sleep
randint(1,60)
print(f"{'-'*50}")
print(f"{"JOGA NA MEGA SENA":^50}")
print(f"{'-'*50}")
q = 10 #int(input("Quantos jogos você quer que eu sorteie? ")) #3 [[6 numeros], [6 numeros], [6 numeros]]
print(f"{f" SORTEANDO {q} JOGOS ":=^50}") 
k = []
t = [[] for i in range(0,q)]
u = []
n = []
p = 0
limbo = 0
#[[6 numeros diferentes]]
for i in range(0,q): #Números
    for j in range(0,6): #Lista interna
        p = len(t[i])-1
        r = len(t[i])-1
        t[i].append(randint(1,60))
        print(t[i]) #lista de números
        #print("t[i][j]: ",t[i][j])
        #print("t[i][j::-1]: ",t[i][j::-1]) #Cada número
        while t[i][t[i].index(max(t[i]))] != t[i][len(t[i])-1]: #numero atual maior que numero anterior
            print(f"{t[i]} {t[i][r]} é o maior número. Subindo posição até a última...")
            #sleep(2)
            limbo = t[i][t[i].index(max(t[i]))]
            t[i][t[i].index(max(t[i]))] = t[i][r+1]
            t[i][r+1] = limbo
            if len(t[i]) == 6:
                print("Limite atingido")
                #sleep(2)
                for k in range(1,len(t[i])):
                    v = len(t[i])-2
                    while v > 0:
                        while t[i][v] == t[i][v-1]:
                            print(f"Sim, {t[i][v]} é igual a {t[i][v-1]}. Substituindo...")
                            temp = t[i][v]
                            t[i][v] = randint(1,60)
                        v = v - 1
            while r > 0 and t[i][t[i].index(min(t[i]))] != t[i][0]:
                print(f"{t[i]} {t[i][r]} é o menor número. Descendo posição até a primeira.")
                limbo = t[i][t[i].index(min(t[i]))]
                t[i][t[i].index(min(t[i]))] = t[i][r-1]
                t[i][r-1] = limbo
                if len(t[i]) == 6:
                    print("Limite atingido")
                    #sleep(2)
                    for k in range(1,len(t[i])):
                        v = len(t[i])-2
                        while v > 0:
                            while t[i][v] == t[i][v-1]:
                                print(f"Sim, {t[i][v]} é igual a {t[i][v-1]}. Substituindo...")
                                temp = t[i][v]
                                t[i][v] = randint(1,60)
                            v = v - 1
                r = r - 1
        while r > 0 and t[i][t[i].index(min(t[i]))] != t[i][0]:
            print(f"{t[i]} {t[i][r]} é o menor número. Descendo posição até a primeira.")
            limbo = t[i][t[i].index(min(t[i]))]
            t[i][t[i].index(min(t[i]))] = t[i][r-1]
            t[i][r-1] = limbo
            if len(t[i]) == 6:
                print("Limite atingido")
                #sleep(2)
                for k in range(1,len(t[i])):
                    v = len(t[i])-2
                    while v > 0:
                        while t[i][v] == t[i][v-1]:
                            print(f"Sim, {t[i][v]} é igual a {t[i][v-1]}. Substituindo...")
                            temp = t[i][v]
                            t[i][v] = randint(1,60)
                        v = v - 1
            while t[i][t[i].index(max(t[i]))] != t[i][len(t[i])-1]: #numero atual maior que numero anterior
                print(f"{t[i]} {t[i][r]} é o maior número. Subindo posição até a última...")
                #sleep(2)
                limbo = t[i][t[i].index(max(t[i]))]
                t[i][t[i].index(max(t[i]))] = t[i][r+1]
                t[i][r+1] = limbo
                if len(t[i]) == 6:
                    print("Limite atingido")
                    ##sleep(2)
                    for k in range(1,len(t[i])):
                        v = len(t[i])-2
                        while v > 0:
                            while t[i][v] == t[i][v-1]:
                                print(f"Sim, {t[i][v]} é igual a {t[i][v-1]}. Substituindo...")
                                temp = t[i][v]
                                t[i][v] = randint(1,60)
                            v = v - 1
            r = r - 1
        p = p - 1
        print(f"t[{i}]: {t[i]}")
        #sleep(2)
    n.append(t[i])
t.clear()
print(t)
print(n)