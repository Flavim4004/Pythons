import random
v=["Vermelho","Preto","Branco"]
din=float(input("Quanto tu tem na conta fih? \n"))
for cont in range(0,999,1):
    
    s=v[random.randint(0,2)]
    aposta=float(input("Quando voce quer aposta fih? \n"))
    if(aposta > din):
        break
    cor=int(input("Escolha uma cor fih! \n [0]Vermelho \n [1]Preto \n [2]Branco \n"))
    din=din-aposta
    if(cor == 0 and s == "Vermelho"):
        mult=aposta*2
        din=din+mult
    elif(cor == 1 and s == "Preto"):
        mult=aposta*2
        din=din+mult
    elif(cor == 2 and s == "Branco"):
        mult=aposta*14
        din=din+mult
    perg=int(input("Voce quer tentar de novo fih? \n [1]Sim [2]Não \n"))
    if(perg == 1):
        print(f"Seu saldo ficou {din} \n")
    
    if(perg == 2):
        print(f"Seu saldo ficou {din} \n")
        break
    if(din == 0):
        break
        
