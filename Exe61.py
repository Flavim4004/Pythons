num=int(input("Digite o numero final da contagem fih! \n "))
cont=(0)
while(cont < num):
    cont=cont+1
    print("{} -- ".format(cont),end="")
    
    if(cont %3 == 0):
        print("PIN\n")
    