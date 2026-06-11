primeiro = int(input("Digite o primeiro termo: "))
quantidade = int(input("Digite a quantidade de termos: "))
razao = int(input("Digite a razão: "))

termo = primeiro

for i in range(quantidade):
    print(termo)
    termo = termo + razao
    