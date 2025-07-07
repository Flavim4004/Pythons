import random
cont=int(0)
din=float(input("Quanto voce tem na conta fih! \n"))
for cont in range(0,99999,1):
    cont=cont+1
    s=random.randint(1,100)
    aposta=float(input("Quanto tu quer apostar fih? \n"))
    if(aposta>din):
        break
    mult=int(input("Escolha um multiplicador fih! \n [1]1.1 \n [2]1.3 \n [3]1.6 \n [4]2.0 \n [5]2.5 \n"))
    din=din-aposta
    if(mult == 1 and (s <= 90 or cont == 1)):
        mult1=aposta*1.1
        din=din+mult1
    elif(mult == 2 and (s <= 80 or cont == 1)):
        mult2=aposta*1.3
        din=din+mult2
    elif(mult == 3 and (s <= 50 or cont == 1)):
        mult3=aposta*1.6
        din=din+mult3
    elif(mult == 4 and (s <= 40 or cont == 1)):
        mult4=aposta*2.0
        din=din+mult4
    elif(mult == 5 and (s <= 20 or cont == 1)):
        mult5=aposta*2.5
        din=din+mult5
    perg=int(input("Voce quer tentar de novo fih? \n [1]Sim [2]Não \n"))
    if(perg == 1):
        print(f"Seu saldo ficou {din} \n")
    
    if(perg == 2):
        print(f"Seu saldo ficou {din} \n")
        break
    if(din == 0):
        break