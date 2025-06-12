num1=int(input("Digite um numero fih! \n"))
num2=int(input("Digite um outro numero fih \n"))
num3=int(input("Digite mais um numero fih! \n"))
maior=int(0)
menor=(0)
meio=(0)
if(num1 > num2 and num1 > num3 and  num2 > num3):
    maior=num1
    meio=num2
    menor=num3
if(num1>num2 and num1 > num2 and num3 > num2):
    maior=num1
    meio=num3
    menor=num2
if(num2 > num1 and num2 >num3 and num1>num3):
    maior=num2
    meio=num1
    menor=num3
if(num2 > num1 and num2 > num3 and num3>num1):
    maior=num2
    meio=num3
    menor=num1
if(num3 > num1 and num3 > num2 and num1 > num2):
    maior=num3
    meio=num1
    menor=num2
if(num3 > num1 and num3 > num2 and num2 > num1):
    maior=num3
    meio=num2
    menor=num1
print("O maior é " + str(maior) + " o meio é " + str(meio) + " ja o menor é " + str(menor))
