"""
teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
#print(teste) #["Gustavo", 40]
galera.append(teste[:]) #uma cópia #resolução #galera.append(teste) --> Ligação entre as duas estruturas
#print(galera) #[["Gustavo", 40]]
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:]) #uma cópia #resolução #galera.append(teste) --> Ligação entre as duas estruturas
print(galera) #[["Gustavo", 40], ['Maria', 22]]
"""
"""
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera) #[['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0]) #['João', 19]
print(galera[0][0]) #'João'
print(galera[2][1]) #13
for p in galera:
    print(p)
    '''
    ['João', 19]
    ['Ana', 33]
    ['Joaquim', 13]
    ['Maria', 45]
    '''
for p in galera:
    print(p[0])
    '''
    ['João', 19]
    ['Ana', 33]
    ['Joaquim', 13]
    ['Maria', 45]
    '''
for p in galera:
    print(p[1])
    '''
    19
    33
    13
    45
    '''
for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade.")
    '''
    João tem 19 anos de idade.
    Ana tem 33 anos de idade.
    Joaquim tem 13 anos de idade.
    Maria tem 45 anos de idade.
    '''
"""
"""
galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #adiciona cópia de dado em galera
    dado.clear() #exclui dado
print(galera) #Exemplo: [['Pedro', 22], ['Maria', 33], ['Claudia', 55]]
"""
"""
galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado) #Se esquecer de digitar galera.append(dado[:]) ----> [:] *Não esqueça esses 3 caracteres
    dado.clear() #Vai gerar listas vazias
#Exemplo: [['Ana', 11], ['Zé', 22], ['Clau', 33]]
print(galera) #[[], [], []] #Listas vazias
"""

galera = list() #Estrutura principal
dado = list() #Estrutura auxiliar pegar os dados antes de salvar na estrutura principal
totmai = totmen = 0 #Total de maior e menor de idade
for c in range(0,3): #Ler os dados e salvar em galera, apagando os dados em cada laço
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #adiciona cópia de dado em galera
    dado.clear() #Limpa dado
#print(galera) #Exemplo: [['Pedro', 22], ['Maria', 33], ['Claudia', 55]]
for p in galera: #Analisa se é maior ou maior de idade
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.') #Cleiton é maior de idade. Caio é maior de idade.
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.') #Eliane é menor de idade.
        totmen += 1
#Totaliza quantidade de menores e maiores de idade. #Exemplo usado: [["Cleiton", 23], ["Eliane", 11], ["Caio", 35]]
print(f"Temos {totmai} maiores e {totmen} menores de idade.") #Temos 2 maiores e 1 menores de idade.