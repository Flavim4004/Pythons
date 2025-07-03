sal=float(input("Quanto tu tem na conta fih? \n"))
com1=float(input("Quando voce vai gastar nesse produto fih? \n"))
com2=float(input("Quanto voce vai gastar nesse outro produto fih? \n"))
soma=float(com1+com2)
des=float(sal-soma)
if(sal < soma):
    print("False")
else:
    print("Verdadeiro")