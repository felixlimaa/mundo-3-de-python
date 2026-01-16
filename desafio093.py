jogador = {}
jogador['nome'] = str(input()).strip().capitalize()
jogador['partidas'] = int(f'Quantas partidas {jogador["nome"]} jogou? ')
for p in range(0,jogador['partidas']):
    jogador['gols'] = int(input(f"Quantos gols {jogador['nome']} fez na partida {p}? "))
print(jogador)