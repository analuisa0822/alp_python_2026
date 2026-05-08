from math import sqrt
x1 = float(input("Digite o primeiro número x:"))
y1 = float(input("Digite o primeiro número y:"))

x2 = float(input("Digite o segundo número x:"))
y2 = float(input("Digite o segundo número y:"))

d = sqrt((x1+y1)**2 + (x2+y2)**2)

print(f"O resultado da soma dos pontos é: {d:.2f}")

