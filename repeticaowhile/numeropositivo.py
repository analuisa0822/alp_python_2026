print("olá, Seja Bem vindo(a)!")
num1= float(input("digite o primeiro numero:"))
num2= float(input("digite o segundo numero:"))

while num1<=0 or num2<=0:
    print("Numero invalido, digite novamente.")
    num1= float(input("digite o primeiro numero:"))
    num2= float(input("digite o segundo numero:"))

print("""
    ----------------------------MENU-------------------------
      1- Média ponderada , com pesos 2 e 3, respectivamente
      2- Quadrado da soma dos 2 números
      3- Cubo do menor número
      4- Escolha uma opção:
      """)


op=int(input("escolha uma opção (1/2/3):"))

if op==1:
    media=((num1*2) + (num2*3))/5
    print(f"O resultado do seu cauculo é:{media:.2f}")
elif op==2:
    qua= (num1+num2)**2
    print(f"O resultado do seu cauculo é:{qua:.2f}")
elif op==3:
    menor= min(num1,num2)
    cubo= menor**3
    print(f"O resultado do seu cauculo é:{cubo:.2f}")
else:
    print("Número inválido")
    quit()

