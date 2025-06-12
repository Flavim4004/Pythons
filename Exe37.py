ano=int(input("Que ano estamos fih ? \n"))
if(ano %4==0  and ano %100 != 0) or (ano %400 == 0):
    print("Bixesto")
else:
    print("Não é bixesto")
