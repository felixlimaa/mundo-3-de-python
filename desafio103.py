def ficha(nome='<desconhecido>', gols=0):
    print('-'*25)
    try:
        n = str(input("Nome do jogador: ")).strip()
        g = int(input("Número de gols: "))
    except ValueError:
        n = nome
        g = gols
    out = print(f'O jogador {n} fez {g} gol(s) no campeonato.')
    return out
ficha() 