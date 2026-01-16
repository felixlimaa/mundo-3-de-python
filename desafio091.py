from random import randint
player = {}
jogo = []
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
#jogo = [{'Jogador': 'Jogador 1', 'Dado': 2}, {'Jogador': 'Jogador 2', 'Dado': 3}, {'Jogador': 'Jogador 3', 'Dado': 6}, {'Jogador': 'Jogador 4', 'Dado': 2}]
rank = {}
p = q = len(jogo)-1
while p > 0:
    while jogo[p]['Dado'] < jogo[p-1]['Dado']: #posicoes internas
        rank['temp'] = jogo[p]
        jogo[p] = jogo[p-1]
        jogo[p-1] = rank['temp']
        del rank['temp']
    while jogo[0]["Dado"] > jogo[p]["Dado"]: #primeira posicao e posicoes internas
        rank['temp'] = jogo[0]
        jogo[0] = jogo[p]
        jogo[p] = rank['temp']
    while jogo[len(jogo)-1]["Dado"] < jogo[p]["Dado"]: #ultima posicao e posicoes internas
        rank['temp'] = jogo[len(jogo)-1]
        jogo[len(jogo)-1] = jogo[p]
        jogo[p] = rank['temp']
    p = p - 1
jogo = jogo[::-1]
for i in range(len(jogo)):
    print(f"{i+1}° lugar: ", end="")
    for v in jogo[i].values():
        if isinstance(v, str):
            print(v, end=" ")
        if isinstance(v, (float, int)):
            print(f"com {v}.")