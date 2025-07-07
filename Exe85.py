cont=int(0)
contA=int(0)
contB=int(0)
contC=int(0)
while(cont!=4):
    nome=str(input("Qual seu nome fih? \n"))
    gasto=float(input("Quanto tu gastou fih? \n"))
    if(gasto>1000):
        contA=contA+1
    elif(gasto>=500 and gasto<=999):
        contB=contB+1
    elif(gasto<499):
        contC=contC+1
    caixa=int(input("Voce quer fechar o caixa fih! \n [1]Sim \n [2]Não \n"))
    if(caixa == 1):
        break
print(f"A quantidade de clientes A e {contA} \n A quantidade de clientes B e {contB} \n A quantidade de clientes c e {contC}")