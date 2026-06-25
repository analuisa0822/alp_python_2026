print("Olá, Seja bem vindo(a)!")

nome = input("Digite o nome do produto: ")
preco= float(input("Digite o preço do produto:"))
quan = int(input("Qual a quantidade no estoque:"))
promo = input("Indique se o produto está em promoção[S/N]:") == "S"

dados = [nome,preco,quan,promo]

print(f"Nome:{dados [0]}")
print(f"Preço:{dados[1]}")
print(f"Quantidade:{dados [2]}")
if promo == True:
    print(f"Está em promoção: sim")
else:
    print(f"Está em promoção: não")