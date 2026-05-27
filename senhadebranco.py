print("Olá,Seja bem vindo(a)!")

nome = input("Digite seu nome: ")

senha_correta = 123456
tentativas = 3

while tentativas > 0:

    senha = int(input("Digite sua senha: "))

    if senha == senha_correta:
        print(f"Olá, {nome}. Seja bem-vindo(a) ao nosso banco!")
        break

    else:
        tentativas = tentativas - 1

        if tentativas == 2:
            print("Senha incorreta! Você ainda tem 2 tentativas.")

        elif tentativas == 1:
            print("Senha incorreta! Você ainda tem 1 tentativa.")

        elif tentativas == 0:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")