print("Olá, Seja bem vinda")

soma=1
cont=0
maior =0 
num = 1
while num >0:
    num = int(input("Digite o número inteiro positivo:"))
    if num >0:
        soma += num
        cont +=1
    if num > maior:
        maior = num 

print(f"A soma é:{soma}")
print(f'A média é:{soma/cont:.1f}')
print(f"O maior é:{maior}")