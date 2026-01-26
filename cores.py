def design(texto, p='nenhum', c='', b=''):
    """
    -----------------------------------------
    ESTILIZAÇÃO DE TEXTOS E NÚMEROS NO TERMINAL
    -----------------------------------------
    Argumentos:
    --> texto é do tipo string, por exemplo: design('Olá Mundo!').
    -----------------------------------------
    Retorno para o Mundo Externo do Código (return):
    --> return: retorna texto estilizado, conforme orientado pelo usuário, no escopo global.
    -----------------------------------------
    Modo de uso do parâmetro p:
    --> p='nenhum': texto sem alterações
    --> p='negrito': texto em negrito
    --> p='underline': texto com linha abaixo
    --> p='invertido': texto com estilo invertido
    ----> cuidado para não digitar a cor(c) no lugar do estilo (p).
    ----> Por exemplo: design('texto', "amarelo")
    ----> Isso ocasionará em erros.
    ----> Caso não defina o estilo, chame o parâmetro c.
    ----> Exemplo: design('texto', c='amarelo')
    ------> Isso garantirá o funcionar correto da função.
    -----------------------------------------
    Modo de uso do parâmetro c:
    O parâmetro c escolhe a cor aplicada ao texto (Por exemplo: "branco") ou ao fundo dele (Por exemplo: "fundo branco").
    -----------------------------------------
    COLORAÇÃO DO TEXTO
    --> c='': mantém cor padrão do terminal
    --> c='branco': deixa o texto branco
    --> c='vermelho': deixa o texto vermelho
    --> c='verde': deixa o texto verde
    --> c='amarelo': deixa o texto amarelo
    --> c='azul': deixa o texto azul
    --> c='roxo': deixa o texto roxo
    --> c='magenta': deixa o texto magenta
    --> c='cinza': deixa o texto cinza
    -----------------------------------------
    COLORAÇÃO DO FUNDO DO TEXTO
    -----------------------------------------
    --> c='fundo branco': deixa o fundo do texto branco
    --> c='fundo vermelho': deixa o fundo do texto vermelho
    --> c='fundo verde': deixa o fundo do texto verde
    --> c='fundo amarelo': deixa o fundo do texto amarelo
    --> c='fundo azul': deixa o fundo do texto azul
    --> c='fundo roxo': deixa o fundo do texto roxo
    --> c='fundo magenta': deixa o fundo do texto magenta
    --> c='fundo cinza': deixa o fundo do texto cinza
    -----------------------------------------
    Modo de uso do parâmetro b:
    --> b='': mantém cor de fundo padrão do terminal
    --> Ele serve para personalizar cor de fundo (b) sem alterar a cor do texto (c).
    ----> Exemplo: print(design("Teste", c='roxo', b='fundo verde'))
    --------------------------------------------------------
    Criado por Felix Lima para treinar funções, dicionários colorir textos no terminal mais rapidamente.
    """

    def estilo(p):
        style = {
            'nenhum': 0,
            'negrito': 1,
            'underline': 4,
            'invertido': 7
        }
        estilo = style[p]
        return estilo

    def cor(c):
        color = {
            "branco": 30,
            "vermelho": 31,
            "verde": 32,
            "amarelo": 33,
            "azul": 34,
            "roxo": 35,
            "magenta": 36,
            "cinza": 37,
            'fundo branco': 40,
            'fundo vermelho': 41,
            'fundo verde': 42,
            'fundo amarelo': 43,
            'fundo azul': 44,
            'fundo roxo': 45,
            'fundo magenta': 46,
            'fundo cinza': 47
        }
        cor = color[c]
        return cor
    
    abreCor = "\033["
    fechaCor = "m"
    limiteCor = "\033[m"
    peso = estilo(p)
    if c in '':
        if b in '':
            e = f"{abreCor}{peso}{fechaCor}{texto}{limiteCor}"
        else:
            corBgFinal = cor(b)
            e = f"{abreCor}{peso};{corBgFinal}{fechaCor}{texto}{limiteCor}"
    elif c not in '':
        corFinal = cor(c)
        if b in '':
            e = f"{abreCor}{peso};{corFinal}{fechaCor}{texto}{limiteCor}"
        else:
            corBgFinal = cor(b)
            e = f"{abreCor}{peso};{corFinal};{corBgFinal}{fechaCor}{texto}{limiteCor}"
    return e

#Testes
#print(design(" Teste ", 'negrito', 'roxo', 'fundo verde'))
#print(design("Olá Mundo!"))
#print(f"Quem é aquele homem todo {design('colorido', 'negrito', 'magenta')}?")
#help(design)
#print('\033[41mOlá Mundo!\033[m')
#print('\033[0;41mOlá Mundo!')