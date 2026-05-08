num= int(input("Digite um número:"))

if num > 0 and num % 2 == 0:
    quad = num**2
    print(f"O resultado do cáuculo é:{quad}")
elif num > 0 and num % 2 == 1:
    cubo = num**3
    print(f"O resultado do caúculo é:{cubo}")
else:
    print("Seu número está invalido")

