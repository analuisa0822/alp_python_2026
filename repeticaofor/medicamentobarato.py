print("Olá , Seja bem vindo(a)!")
soma = 0 
nomebarato = ""
menorpreco = 0

for cont in range(5):
    nome = input("Digite o nome do medicamentos:")
    preco = float(input("Digite o preço do medicamento:"))

    soma += preco 
    if cont == 0:
        nomebarato = nome
        menorpreco = preco

    elif preco < menorpreco:
        nomebarato = nome
        menorpreco = preco

media = soma / 5

print("Medicamento mais barato:")
print(f"Nome: {nomebarato}")
print(f"Preço: R${menorpreco:.2f}")

print(f"Média dos preços: R${media:.2f}")

    

        

