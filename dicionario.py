usuarios = {}

quantidade = int(input("Quantos usuários deseja cadastrar? "))

# Cadastro
for i in range(quantidade):
    login = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    usuarios[login] = senha

# Login
usuario_login = input("Usuário: ")
senha_login = input("Senha: ")

if usuario_login in usuarios:
    if usuarios[usuario_login] == senha_login:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não cadastrado!")
