n = [] #números varios
for i in range(0,5): #contagem até 5
    n.append(int(input("Digite um número: "))) #adiciona número em n
    p = len(n)-1 #quantidade de valores em n
    while p > 0 and n[p] < n[p-1]: #se a quantidade de n é maior que zero e o numero atual é menor que o anterior 
        temp = n[p] #manda o numero atual para um limbo temporário
        n[p] = n[p-1] #manda o numero anterior para o banquinho do atual
        n[p-1] = temp #manda o numero que tá no limbo para banquinho do anterior
        print(f"{n[p]} adicionado na posição {p}.") 
        print(f"{n[p-1]} adicionado na posição {p-1}.")
        p = p - 1 #diminua o tamanho por 1 a cada repetição while
    print(f"Números em ordem crescente: {n}")