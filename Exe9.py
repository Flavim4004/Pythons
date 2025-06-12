n1=float(input("Digite um numero fih! \n "))
n2=float(input("Digite outro numero fih! \n"))
peg=int(input("Que formula voce quer usar fih? \n 1.Adicão \n 2.Subtração \n 3.Multiplicação \n 4.Divisão \n "))
if(peg == 1 ):
    cal1=float(n1 + n2)
    print("A soma seria " + str(cal1))
elif(peg == 2):
    cal2=float(n1 - n2)
    print("A subtração seria " + str(cal2))
elif(peg == 3):
    cal3=float(n1 * n2)
    print("A Multiplicação seria " + str(cal3))
elif(peg == 4):
    cal4=float(n1 / n2)
    print("A Divisão seria " + str(cal4))
else:
    print("INVALIDO")