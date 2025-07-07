
contn=int(0)
cont=int(0)
contp=int(0)
while(cont!=999):
    num=float(input("Digite um numero fih! \n"))
    if(num <= 0):
        contn=contn+1
    elif(num > 0):
        contp=contp+1
        soma=(num+num)
    para=int(input("Voce quer para fih? \n [1]Sim \n [2]Não \n "))
    cont=cont+1
    if(para==1):
        break


media=(soma/contp)
print(f"A media dos numeros postivos é {media} ja a sua quantidade é {contp} e a quantidade de negativos é {contn}")    