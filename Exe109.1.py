import random
v=["Pedra","papel","Tesoura","Largato","Spock"]
for cont in range(0,999999,1):
    r=random.randint(0,4)
    s=v[r]
    resp=int(input("Escolha fih! \n [0]Pedra \n [1]Papel \n [2]Tesoura \n [3]Largato \n [4]Spock \n"))
    if(resp==r):
        print("EMPATE!")
        break
    elif((resp==0 and (r==2 or r==3)) or (resp==1 and (r==0 or r ==4)) or (resp==2 and (r==1 or r ==3)) or (resp==3 and (r==1 or r==4)) or (resp==4 and (r==0 or r==2))):
        print("VITORIA!")
        break
    else:
        print("FAMOSO 3 CAPA TROPA AAAA!")
        break
