produtos = []

resposta = "s"

while resposta == "s":
    produto = input("Digite o nome do produto eletrônico: ")
    produtos.append(produto)

    resposta = input("Deseja adicionar outro produto? (S/N): ") .lower()

print("Lista de produtos:")
for nome in produtos:
    print(nome)
    