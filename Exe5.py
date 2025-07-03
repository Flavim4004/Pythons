n1=int(input("Digite um numero fih! \n"))
n2=int(input("Digte outro numero fih! \n"))
n3=int(input("Digte mais um numero fih! \n "))
soma=int(n1+n2)
if(soma <= n3):
    print(" A soma de " + str(n1) + " e " + str(n2) + " e menor que " + str(n3) )
else:
    print("O numero " + str(n3) + " e maior que A soma de " + str(n1) + " e " + str(n2))