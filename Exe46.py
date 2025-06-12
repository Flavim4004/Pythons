compra=float(input("Quando voce vai gastar fih? \n"))
if(compra >= 500.00):
    cal1=float(compra-(compra*0.05))
    print("Como a compra foi maior que 500 receb o desconto ficando " + str(cal1))
else:
    print("A compra de " + str(compra) + " foi cadastrada com sucesso")