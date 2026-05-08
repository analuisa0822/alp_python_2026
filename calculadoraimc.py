print ("""
    -------- Tabela de IMC--------
    menor que 18.5     | Magueza
    entre 18.5 e 24.9  | Peso normal
    entre 25.00 e 29.9 | Sobrepeso
    entre 30.00 e 39.9 | Obesidade
    acima de 40        | Obesidade grave
    -------------------------------
  """)
peso = float(input("Digite seu peso (Kg):"))
altura = float(input("Digite sua altura (m):"))
imc = peso / (altura * altura)

if imc<= 18.5:
    print(f"Magreza")
elif imc<=24.9:
    print(f"Peso normal")
elif imc<=29.9:
    print(f"Sobrepeso")
elif imc<=39.9:
    print(f"Obesidade")
else:
    print(f"Obesidade grave")

print(f"O resuldado do seu imc é: {imc:.2f} ")
