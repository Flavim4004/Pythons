cont=int(0)
soma=int(0)
while(cont != 999):
    num=int(input("Digite um numero fih! \n"))
    cont=cont+1
    soma=soma+num
    
    
    if(num==999):
        break
print(f"Foram feitas {cont} tentativas e a soma dos numeros e {soma}")