from cores import design
def leiaInt(prompt='', /):
    print(prompt, end='')
    leu = input()
    while ValueError:
        try:
            print(int(leu))
            break
        except ValueError:
            print(design("ERRO! Digite um número inteiro válido.", "negrito", "vermelho"))
            print(prompt, end='')
            leu = input()  
    return leu

n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")

#help(input)
"""
input(prompt='', /)
Read a string from standard input.  The trailing newline is stripped.

The prompt string, if given, is printed to standard output without a
trailing newline before reading input.

If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
On *nix systems, readline is used if available.
"""