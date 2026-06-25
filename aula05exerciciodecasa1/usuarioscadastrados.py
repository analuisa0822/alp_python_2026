logins = []
senhas = []

quantidade = int(input("Quantos usuários deseja cadastrar? "))

# Cadastro dos usuários
for i in range(quantidade):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    logins.append(usuario)
    senhas.append(senha)

# Login
usuario_login = input("Usuário: ")
senha_login = input("Senha: ")

if usuario_login in logins:
    indice = logins.index(usuario_login)

    if senhas[indice] == senha_login:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não cadastrado!")