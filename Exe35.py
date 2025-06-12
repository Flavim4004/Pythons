num1=int(input("Digite um numero fih! \n "))
num2=int(input("Digite um numero fih! \n "))
num3=int(input("Digite um numero fih! \n "))
somapar=int(0)
somaimpar=int(0)
if(num1 %2 == 0):
    somapar = somapar + num1
if(num1 %2 == 1):
    somaimpar = somaimpar + num1
if(num2 %2 == 0):
    somapar = somapar + num2
if(num2 %2 == 1):
    somaimpar = somaimpar + num2
if(num3 %2 == 0):
    somapar = somapar + num3
if(num3 %2 == 1):
    somaimpar = somaimpar + num3
print("A soma dos pares e " + str(somapar) + " ja a dos impares é " + str(somaimpar))