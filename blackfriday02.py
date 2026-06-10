import os
print("Proção de black friday.")

print("""
     -----------------------TABELA------------------------------
        codigo | condição de pagamento | desconto (%)
    ------------------------------------------------------------
           1   | Á vista (em espécie)  | 15
           2   | Cartão de débito      | 10
           3   | Cartão de credito     | 5
           0   | Sair do programa      | 
    ------------------------------------------------------------
      
      """)

pag= int (input("Escolha a forma de pagamento(1/2/3/0):"))
while pag !=0:
    preco = float(input("Digite o preço da compra:"))
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
         os.system("clear")
    pag= int (input("Escolha a forma de pagamento(1/2/3/0):"))

    
    

