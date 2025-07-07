cont=int(0)
cont9=int(0)
num = [0,0,0,0]
for cont in range(0,4,1):
    num[cont]=int(input("Digite um numero fih! \n"))
    if(num[cont] == 9):
        cont9=cont9+1
print(f"O numero 9 apareceu {cont9} vezes")