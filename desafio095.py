jogador = {}
time = []
continuar = ""
escolha = 0
"""while True:
    jogador['nome'] = str(input("Digite o nome do jogador: ")).strip().capitalize()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    for p in range(0,jogador['partidas']):
        jogador['gols'].append(int(input(f"Quantos gols {jogador['nome']} fez na partida {p}? ")))
    del jogador["partidas"]
    jogador['total'] = sum(jogador["gols"])
    print("-="*25)
    #print(jogador) # {'nome': 'Joao', 'gols': [0, 1], 'total': 1}
    time.append(jogador.copy())
    jogador.clear()
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        print("Opção inválida! Tente de novo...")
        continuar = str(input("Quer continuar? [S/N]: "))
    if continuar in "N":
        break
print(time) #[{'nome': 'Kalel', 'gols': [1, 3], 'total': 4}, {'nome': 'Maico', 'gols': [1, 0, 3, 2, 0, 1], 'total': 7}, {'nome': 'Gabriel', 'gols': [1, 0, 2], 'total': 3}]
print("-="*25)
"""

time = [{'nome': 'Kalel', 'gols': [1, 3], 'total': 4}, {'nome': 'Maico', 'gols': [1, 0, 3], 'total': 7}, {'nome': 'Gabriel', 'gols': [1, 0, 2], 'total': 3}]
#print(time)
print('cod', end=" ")
for k in time[escolha].keys():
    print(f"{k:<10}", end=" ")
print()
print("-"*35)
for c in range(0,len(time)):
    print(f"{c:>3}", end=" ")
    for v in time[c].values():
        if isinstance(v, (str, float, int)):
            print(f"{v:<10}", end=" ")
        else:
            print(f"{v}", end="")
            print(f"{'':^5}", end="")
    print()
#escolha = int(input("Mostrar dados de qual jogador? "))
#print(time[escolha].values())

"""
    print("-="*25)
    for d, v in jogador.items():
        print(f"O campo {d} tem o valor {v}.")
    print("-="*25)
    print(f"O jogador {jogador['nome']} jogou {len(jogador["gols"])} partidas.")
    for i in range(0,len(jogador['gols'])):
        print(f"  ==> Na partida {i}, fez {jogador["gols"][i]} gols.")
    print(f"Foi um total de {jogador["total"]} gols.")
"""