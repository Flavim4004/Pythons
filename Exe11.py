preco=float(input("Digite o valor que voce vai gastar no produto fih! \n"))
resp=int(input("Em que epoca estamos fih? \n [1]Carnaval \n [2]Ferias \n [3]Dia das crianças \n [4]Black friday \n [5]Natal \n "))
if(resp==1):
    cal1=float(preco+(preco*0.10))
    print("O novo preço é " + str(cal1))
elif(resp==2):
    cal2=float(preco+(preco*0.20))
    print("O novo preço é " + str(cal2))
elif(resp==3):
    cal3=float(preco+(preco*0.05))
    print("O novo preço é " + str(cal3))
elif(resp==4):
    cal4=float(preco-(preco*0.30))
    print("O novo preço é " + str(cal4))
elif(resp==5):
    cal5=float(preco-(preco*0.05))
    print("O novo preço é " + str(cal5))
else:
    print("O preço e o mesmo \n " + str(preco))
