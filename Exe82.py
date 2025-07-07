cont=int(0)
soma=int(0)
while(cont !=99999):
    num=int(input("Digite um numero fih! \n"))
    cont=cont+1
    soma=soma+num
    if(num==999):
        break
print(f"A soma dos numeros é {soma} ja as tentativas feitas são {cont}")