jogador = {}
time = []
continuar = ""
escolha = 0
while True:
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
#time = [{'nome': 'Kalel', 'gols': [1, 3], 'total': 4}, {'nome': 'Maico', 'gols': [1, 0, 3], 'total': 7}, {'nome': 'Gabriel', 'gols': [1, 0, 2], 'total': 3}]
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
while escolha != 999 and escolha <= len(time)-1:
    print("--"*25)
    escolha = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    while escolha > len(time)-1 and escolha < 999:
        print(f"ERRO: Não existe jogador com código {escolha}. Tente de novo!")
        escolha = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if escolha == 999:
        break
    print(f"— LEVANTAMENTO DO JOGADOR ", end="")
    for v in time[escolha].values():
        if isinstance(v,str):
            print(v)
        if isinstance(v,list):
            for c in range(len(v)):
                print(f"No jogo {c}, fez {v[c]} gols.")
print("<< VOLTE SEMPRE >>")