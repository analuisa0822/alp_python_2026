n1= float(input("Informe a primeira nota do bimestre 1 (0-10):"))
n2= float(input("Informe a segunda nota do bimestre 2 (0-10):"))
n3=float(input("Informe a terceira nota do bimestre 3 (0-10)"))

media = (n1 + n2 + n3) / 3
print(f"O valor da sua média é: {media:.1f}")

if media >= 7:
    print("Aprovado(a)")
elif media >= 4:
    print("Prova final")        
else: 
    print("Reprovado(a)")
