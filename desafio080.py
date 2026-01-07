ordem = numeros = ant = atual = []
numeros = [12, 2, 4, 10, 45] #Tenho a sequência
numeros.append(34) #Adiciono um novo número
#print(numeros) #Lista atualizada
contador = semicontador = 1
while contador != 5:
    ultimo = numeros[len(numeros)-contador] #[12, 2, 4, 10, 45, 34] #Seleciona o último item adicionado #Posição 5
    #Seleciona cada um dos itens anteriores
    for i in enumerate(numeros):
        anterior = numeros[len(numeros)-(contador+1)] #Posição 4 #[12, 2, 4, 10, 45]
        #print(f"Anterior: {anterior}")
        #print(f"numeros[{len(numeros)}-{i}]: {anterior}")
        if ultimo < anterior: #[12, 2, 4, 10, 45, 34]
            for c in range(0,contador): #Conte até 2
                temp = anterior
                numeros.remove(anterior) #[12, 2, 4, 10, 34]
                #print(f"Anterior removido: {numeros}")
                numeros.append(temp) #[12, 2, 4, 10, 34, 45]
                #print(f"Anterior adicionado por último: {numeros}")
                ultimo = numeros[len(numeros)-(contador+1)] #Posição de análise alterada de 5 para 4
        elif ultimo > anterior: #[12, 2, 4, 10, 34]
            #Muda a posição do anterior para análise
            print(f"Analisando último na posição {numeros.index(ultimo)}") #Posição 4
            anterior = numeros[len(numeros)-(contador+2)] #Posição 3
            print(f"Analisando anterior na posição {numeros.index(anterior)}")
            if ultimo < anterior: #[12, 2, 4, 10, 45, 34]
                for c in range(0,contador): #Conte até 2
                    temp = anterior
                    numeros.remove(anterior) #[12, 2, 4, 10, 34]
                    #print(f"Anterior removido: {numeros}")
                    numeros.append(temp) #[12, 2, 4, 10, 34, 45]
                    #print(f"Anterior adicionado por último: {numeros}")
                    ultimo = numeros[len(numeros)-(contador+1)] #Posição de análise alterada de 5 para 4
    contador += 1
    print(f"Contador: {contador}")
    print(f"Números: {numeros}") #[2, 4, 10, 34, 45, 12]
"""
while i < 5:
    print(f"numeros[{i}::-1]: {numeros[i::-1]}") #inverte
    i += 1
"""
"""for i in range(0, 5):
    a = numeros.append(int(input("Digite um número: ")))
    b = numeros[:]
    print(f"Números digitados: {numeros}")
    print(f"i: {i}")
    print(f"b: {b}")
    if len(numeros) > 1:
        print(numeros)"""