import os
print("""
      *************Calculadora**************
      Escolha sua operação
      1.Soma
      2.Subtração
      3.Multiplicação
      4.Divisão
      0.Sair
      **************************************
      """)

operacao = int(input("Escolha uma operação (0/1/2/3/4):"))
while operacao !=0:
  num1 = float(input("Digite o primeiro número:"))
  num2= float(input("Digite o segundo número:"))
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
    resultado = num1/num2
    print(f"O resultado é:{resultado}")
  else:
    os.system("clear")
  operacao=int(input("Esconha uma operação(0/1/2/3/4):"))