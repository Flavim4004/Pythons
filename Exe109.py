import random
v=["Pedra","papel","Tesoura"]
for cont in range(0,999999,1):
    s=v[random.randint(0,2)]
    resp=int(input("Escolha fih! \n [1]Pedra \n [2]Papel \n [3]Tesoura  \n"))
    if(s == "Pedra" and resp == 1 ):
        print("EMPATE! \n")
        print(f"ESCOLHA DA IA:{s} ESCOLHA DO USUARIO:PEDRA ")
        break
    if(s == "Pedra" and resp == 2):
        print("Usuario GANHOU! \n")
        print(f"ESCOLHA DA IA:{s} ESCOLHA DO USUARIO:PAPEL ")
        break
    if(s == "Pedra" and resp == 3):
        print("IA:SO CAPA! \n")
        print(f"ESCOLHA DA IA:{s} ESCOLHA DO USUARIO:TESOURA ")
        break
    if(s == "papel" and resp == 1):
        print("IA:AVE MARIA! \n")
        print(f"ESCOLHA DA IA:{s} ESCOLHA DO USUARIO:PEDRA ")
        break
    if(s == "papel" and resp == 2):
        print("EMPATE! \n")
        print(f"ESCOLHA DA IA:{s} ESCOLHA DO USUARIO:PAPEL ")
        break
    if(s == "papel" and resp == 3):
        print("Usuario GANHOU! \n")
        print(f"ESCOLHA DA IA:{s} ESCOLHA DO USUARIO:TESOURA ")
        break
    if(s =="Tesoura" and resp == 1):
       print("Usuario GANHOU! \n")
       print(f"ESCOLHA DA IA:{s} ESCOLHA DO USUARIO:PEDRA ")
       break
    if(s == "Tesoura" and resp ==2):
        print("IA:AIIII NOBRU APELÃO! \n")
        print(f"ESCOLHA DA IA:{s} ESCOLHA DO USUARIO:PAPEL ")
        break
    if(s == "Tesoura" and resp ==3):
        print("EMPATE \n")
        print(f"ESCOLHA DA IA:{s} ESCOLHA DO USUARIO:TESOURA ")
        break


