cont=int(0)
somapar=int(0)
somaimpar=int(0)
while(cont != 5):
    num=int(input("Digite um numero fih! \n "))
    if(num %2 == 0):
        somapar=somapar+num
    elif(num %2 == 1):
        somaimpar=somaimpar+num
    else:
        print("")
    cont=cont+1
print(f"A soma dos numeros pares é {somapar} ja a dos numeros impares é {somaimpar}")