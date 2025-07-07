cont=int(0)
cont2=int(0)
cont3=int(0)
cont4=int(0)
cont5=int(0)
while(cont != 9999):
    num=int(input("Digite um numero fih! \n"))
    if(num <= 25):
        cont2=cont2+1
    elif(num >25 and num <=50):
        cont3=cont+1
    elif(num >50 and num <=75):
        cont4=cont4+1
    elif(num >76 and num <=100):
        cont5=cont5+1
    else:
        print("")
    parou=int(input("Tu quer para fih? \n [1]Sim \n [2]Não \n"))
    if(parou==1):
        break
print(f"A contagen de numeros \n menores que 25 deu {cont2} \n entre 26 e 50 {cont3} \n entre 51 e 75 {cont4} \n entre 76 e 100 {cont5} ")