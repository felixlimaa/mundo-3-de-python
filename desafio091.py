from random import randint
"""player = {}
jogo = []
temp = []
for i in range(1,5):
    player['Jogador'] = f"Jogador {i}"
    player['Dado'] = randint(1,6)
    jogo.append(player.copy())
    #print(jogo) #[{'Jogador': 'Jogador 1', 'Dado': 6}, {'Jogador': 'Jogador 2', 'Dado': 4}, {'Jogador': 'Jogador 3', 'Dado': 5}, {'Jogador': 'Jogador 4', 'Dado': 5}]
print("Valores sorteados:")
for j in jogo:
    print(f"O ", end="")
    for v in j.values():
        if isinstance(v,str):
            print(v, end=" ")
        if isinstance(v,int):
            print("tirou", end=" ")
            print(f'{v}.', end=" ")
    print()
print("Ranking dos jogadores:")
rank = []
for i in range(0,len(jogo)):
    p = len(jogo)-1
    dado = [j['Dado'] for j in jogo]
print(jogo)"""
jogo = [{'Jogador': 'Jogador 1', 'Dado': 2}, {'Jogador': 'Jogador 2', 'Dado': 3}, {'Jogador': 'Jogador 3', 'Dado': 6}, {'Jogador': 'Jogador 4', 'Dado': 2}]
rank = []
dado = [j['Dado'] for j in jogo]
print(dado) #[2, 3, 6, 2]
print(min(dado))
#Método Copy
p = len(jogo)-1
while p > -1:
    print(min)
    if jogo[p]['Dado'] == min(dado):
        rank.append(jogo[p].copy())
        print(f"jogo: {len(jogo)}",jogo)
        print(f"rank: {len(rank)}",rank)
        del jogo[p]
        p = p - 1
        print("p: ",p)
print(f"jogo: {len(jogo)}",jogo)
print(f"rank: {len(rank)}",rank)