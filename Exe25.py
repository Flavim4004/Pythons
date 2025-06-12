n1=int(input("Digite um numero fih! \n"))
n2=int(input("Digite outro numero fih \n"))
n3=int(input("digite mais um numero fih \n"))
contpar=int(0)
contimpar=int(0)
if(n1 %2 == 0):
    contpar = contpar + 1
if(n2 %2 == 0):
    contpar = contpar + 1
if(n3 %2 == 0):
    contpar = contpar + 1
if(n1 %2 == 1):
    contimpar = contimpar + 1
if(n2 %2 == 1):
    contimpar = contimpar + 1
if(n3 %2 == 1):
    contimpar = contimpar + 1
print("Foram encontrados " + str(contpar) + " numeros pares é " + str(contimpar) + " numeros impares")
