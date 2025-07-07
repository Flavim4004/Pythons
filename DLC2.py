cont=int(0)
produtos=[]
for cont in range(0,99999,1):
    compra=str(input("Qual produto voce quer comprar fih! \n"))
    produtos.append(compra)
    parar=int(input("Voce quer parar? \n [1]Sim [2]Não \n"))
    if(parar==1):
        print(produtos)
        break
    else:
        print(produtos)
