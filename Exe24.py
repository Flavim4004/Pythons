num1=int(input("Escolha um numero fih! \n"))
num2=int(input("Escolha um outro numero fih! \n"))
soma=int(num1+num2)
media=int(soma/2)
a=int(input("Voce quer fazer a \n 1.media \n 2.soma \n desses numeros \n "))
if(a == 1):
    print("Média de " + str(num1) + " e " + str(num2) + " é igual a " + str(media))
if(a == 2):
    print("A soma de " + str(num1) + " e " + str(num2) + " é igual a " + str(soma))
