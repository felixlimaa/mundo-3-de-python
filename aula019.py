pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}
print(pessoas) #{"nome": "Gustavo", "sexo": "M", "idade": 22}
print(pessoas['nome']) #Gustavo
print(pessoas['idade']) #22
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.") #O Gustavo tem 22 anos.
print(pessoas.keys()) #dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) #dict_values(['Gustavo', 'M', 22])
print(pessoas.items()) #dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
for k in pessoas.keys():
    print(k)
    """
    nome
    sexo
    idade
    """
for k in pessoas.values():
    print(k)
    """
    Gustavo
    M
    22
    """
for k, v in pessoas.items():
    print(f"{k} = {v}")
    """
    nome = Gustavo
    sexo = M
    idade = 22
    """
#20:15