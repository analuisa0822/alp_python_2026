print(""" 
      **** Calculadora de Números reais ****
      1.Soma
      2.Subtração
      3.Multiplicação
      4.Divisão
      **************************************
      Escolha sua operação
      1.Soma
      2.Subtração
      3.Multiplicação
      4.Divisão
      """)

operacao = int(input("Escolha a operação (1/2/3/4):"))
num1 = float(input("Digite o primeiro número:"))
num2= float(input("Digite o segundo número:"))

if operacao < 1 or operacao > 4:
    print("Opção inválida!")
if operacao == 1:
    resultado = num1 + num2
    print(f"O resultado da soma é:{resultado}")

elif operacao == 2:
    resultado = num1 - num2
    print(f"O resultado da subtração é:{resultado}")

elif operacao == 3:
    resultado = num1 * num2
    print(f"O resultado da multiplicação é:{resultado}")

elif operacao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é:{resultado}")
    else:
        print("Divisão por Zero! Escolha outro número!")
