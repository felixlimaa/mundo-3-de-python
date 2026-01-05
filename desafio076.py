print("="*50)
print(f"{"Listagem de preços":^50}")
print("="*50)
legado = old = nome = preco = ()
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
for i in range(1):
    nome = (produtos[i::2])
    legado = (*legado, nome)
    preco = (produtos[i+1::2])
    old = (*old, preco)
for i in range(len(nome)):
    print(f"{nome[i]:<10} {"":.^20} R${preco[i]:<10.2f}")