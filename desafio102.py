def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    if show == True:
        for c in range(n, 0, -1):
            if c == 1:
                print(c, end=" ")
            else:
                print(c, end=" x ")
        print('=', end=' ')
    f = 1
    for c in range(n, 0, -1):
        f *= c
    print(f)
    
fatorial(5)
fatorial(3, True)
fatorial(7, True)