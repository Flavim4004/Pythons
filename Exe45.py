num1=int(input("Digite um numero fih! \n"))
num2=int(input("Digite outro numero fih! \n"))
num3=int(input("Digite mais um numero fih! \n"))
soma1=int(num2 + num3)
soma2=int(num1 + num3)
soma3=int(num1 + num2)
if(num1 < soma1 and num2 < soma2 and num3 < soma3):
    print("E triangulo fih")
else:
    print("Não e triangulo fih")