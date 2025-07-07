import random
cont=int(0)
while(cont != 999999):
    num=int(input("Digite um numero de 1 a 10 fih! \n"))
    s=random.randint(1,10)
    cont=cont+1
    if(num > s):
        print(f"Voce errou tente um numero menor fih! \n numero do sorteio:{s} ")
    if(num < s):
        print(f"Voce errou tente um numero maior fih! \n numero do sorteio:{s} ")
    if(num==s):
        print(f"Parabem voce acertou fih! \n numero do sorteio:{s} ")
        break
print(f"Voce precisou de {cont} tentativas para acertar o numero")   
