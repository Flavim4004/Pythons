num1=int(input("Escolha um numero fih! \n"))
num2=int(input("Escolha um numero fih! \n"))
num3=int(input("Escolha um numero fih! \n"))
num4=int(input("Escolha um numero fih! \n"))
contpar=int(0)
somapar=int(0)
maiorpar=int(0)
if(num1 %2 == 0):
    contpar = contpar + 1
    somapar = somapar + num1
if(num1 > maiorpar and num1 %2 == 0):
    maiorpar = num1
if(num2 %2 == 0):
    contpar = contpar + 1
    somapar = somapar + num2
if(num2 > maiorpar and num2 %2 == 0):
    maiorpar = num2
if(num3 %2 == 0):
    contpar = contpar + 1
    somapar = somapar + num3
if(num3 > maiorpar and num3 %2 == 0):
    maiorpar = num3
if(num4 %2 == 0):
    contpar = contpar + 1
    somapar = somapar + num4
if(num4 %2 == 0 and num4 > maiorpar):
    maiorpar = num4
print("o maior numero par é " + str(maiorpar) + " \n ja a quantidade de pares é " + str(contpar) + " \n ja a soma dos numeros pares é " + str(somapar))