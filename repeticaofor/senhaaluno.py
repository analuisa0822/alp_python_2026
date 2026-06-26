#importando a biblioteca operacional system (sistema operacional)
print("Olá, Seja  bem vindo(a)!")

for tentativa in range(1,4):
    usuario = input("Usuario:")
    senha = input ("Senha:")
    if usuario == "aluno" and senha =="12345":
        print("Acesso liberado")
        break
    else:
        print("Tente novamente!")

if tentativa ==3:
    print("Você tentou 3 vezes")