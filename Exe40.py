idade=int(input("Qual sua idade fih? \n"))
if(idade >=18):
    sexo=str(input("Qual seu sexo fih? \n"))
    if(sexo == "masculino"):
        nacao=str(input("Qual sua naçao fih? \n"))
        if(nacao == "Brasil"):
            print("Bem vindo solado")
        else:
            print("Não apto")
    else:
        print("Não apto")
          
else:
    print("Não apto")