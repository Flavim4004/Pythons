resp=int(input("Escolha um humorista fih! \n [1]Fabio Porchat  \n [2]Danilo Gentili \n [3]Rafinha bastos \n "))
resp2=int(input("Escolha a cidade fih! \n [1]São Paulo capital \n [2]Araxá \n [3]Rio Grande do Sul  \n"))
if(resp == 2 and resp2 ==1):
    print("Tem show do Danilo Gentili Fih")

    
elif(resp==1 and resp2==2):
    idade=int(input("Quantos anos tu tem fih? \n"))
    if(idade>=18):
        print("tem show do Fabio Porchat fih" )
    else:
        print("Desculpa fih tu é menor de idade")

    
elif(resp==3 and resp2 == 3):
    cidade=int(input("ele ta na cidade fih? \n [1]Sim \n [2]não \n"))
    if(cidade==1):
        print("tem show do rafinha Bastos")
    elif(cidade==2):
        print("não tem show")
    else:
        print("Desculpa ele nao ta na cidade fih!")
else:
    print("Tente outra vez fih!")
