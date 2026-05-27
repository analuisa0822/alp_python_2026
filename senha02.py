
print("Olá, Seja bem vindo(a)!")
usuario=input("Qual seu usuário:")
senha =input("Digite sua senha:")

quant =0

while (usuario != "aluno" and senha != "12345") and quant <2:
    print("Tente novamente")
    quant+=1

    usuario=input("Qual seu usuário:")
    senha =input("Digite sua senha:")
if quant ==2:

    print("Você tentou 3 vezes")
else:
    print("Acesso liberado")

    