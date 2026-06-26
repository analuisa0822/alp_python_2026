import random

nomes = []

quantidade = int(input("Quantas pessoas compraram a rifa? "))

for i in range(quantidade):
    nome = input("Digite o nome da pessoa: ")
    nomes.append(nome)

ganhador = random.choice(nomes)

print("O ganhador da rifa foi:", ganhador)
