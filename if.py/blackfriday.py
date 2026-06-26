print("Proção de black friday.")
preco = float(input("Digite o preço da compra:"))

print("""
     -----------------------TABELA------------------------------
        codigo | condição de pagamento | desconto (%)
    ------------------------------------------------------------
           1   | Á vista (em espécie)  | 15
           2   | Cartão de débito      | 10
           3   | Cartão de credito     | 5
    ------------------------------------------------------------
      """)

pag= int (input("Escolja a forma de pagamento(1/2/3):"))
if pag == 1:
    porc=(15*preco)/100
    final=preco-porc
    print(f"O valor final a pagar é:{final}")
elif pag == 2:
    porc=(10*preco)/100
    final=preco-porc
    print(f"O valor final a pagar é:{final}")
elif pag == 3:
    porc=(5*preco)/100
    final=preco-porc
    print(f"O valor final a pagar é:{final}")
else:
    print("Numero invalido.")

