print("Olá, Seja bem vindo(a)!")


quant_pares = 0
for cont in range(1,11):
    num = int(input(f"Digite o {cont } número:"))
    if num % 2 == 0: #verifica se e par
        quant_pares += 1 
print(f"Tem {quant_pares} números pares.")
