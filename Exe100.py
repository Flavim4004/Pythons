cont=int(0)
cont14=int(0)
num = [0,0,0,0]
for cont in range(0,3,1):
    num[cont]=int(input("Digite um numero fih! \n"))
    if(num[cont] == 14):
        cont14=cont14+1
print(f"O numero 14 apareceu {cont14} vezes")