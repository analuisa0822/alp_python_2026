import random

numero_sorteado = random.randint(1, 10)

tentativas = 0

while tentativas < 3:
    numero = int(input("Digite um número de 1 a 10: "))
    tentativas = tentativas + 1

    if numero == numero_sorteado:
        print("Parabéns, você acertou!")
        break

    else:
        print("Você errou!")

        if numero > numero_sorteado:
            print("Tente um número menor")
        else:
            print("Tente um número maior")

        if tentativas == 3:
            print("Você perdeu! Fim de jogo.")