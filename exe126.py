import exe126funcoes
media=int(0)
num1=int(input("Digite um numero fih! \n"))
num2=int(input("Digite um numero fih! \n"))
maior=exe126funcoes.valor1(num1,num2)
menor=exe126funcoes.valor2(num1,num2)
soma=maior+menor
media=soma/2
print(f" A média é {media}")