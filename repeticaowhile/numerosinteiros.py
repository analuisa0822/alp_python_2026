soma = 0
quantidade = 0
maior = 0

numero = 0

while numero >= 0:

    numero = int(input("Digite um número positivo: "))

    if numero >= 0:

        soma += numero
        quantidade += 1

        if numero > maior:
            maior = numero
if quantidade > 0:

    media = soma / quantidade

    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media}")
    print(f"Maior número digitado: {maior}")

else:

    print("Nenhum número positivo foi informado!")