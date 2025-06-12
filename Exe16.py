valor=int(input("Quanto tu tem na conta fih?"))
mes=int(input("Quanto tu gastou nesse mês fih?"))
gastos=int(valor-mes)
if( gastos == 0):
    print("Não tem dinheiro")
else:
    print("Tem dinheiro")
