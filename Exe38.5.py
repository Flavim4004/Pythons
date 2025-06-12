hora=float(input("Quantas horas de aula voce deu fih? \n"))
aulas=float(input("Quantas aulas voce deu fih? \n"))
sal=float(hora*aulas)
if(sal<= 1518):
    cal=(sal -(sal * 0.075))
    print("O salario ficou " + str(cal))
if(sal >=1518.01 and sal <=2793.88):
    cal1=(sal-(sal*0.9))
    print("O salario ficou " + str(cal1))
if(sal>= 2793.89 and sal <= 4190.83):
    cal2=(sal-(sal*1.2))
    print("O salario ficou " + str(cal2))
if(sal >= 4190.84 and sal <= 8157.41):
    cal3=(sal-(sal*1.4))
    print("O salario ficou " + str(cal3)) 
if(sal >8157.41):
    print("INVALIDO")
    
