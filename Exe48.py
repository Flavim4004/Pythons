num1=int(input("Digite um numero fih! \n"))
num2=int(input("Digite um outro numero fih! \n"))
if(num1 < num2):
    print(num1,num2)
elif(num2 < num1):
    print(num2,num1)
elif(num1 == num2):
    print("Os numeros são iguais!")
else:
    print("...")