idade=int(input("Qual sua idade fih! \n"))
sexo=str(input("Qual seu sexo fih! \n"))
nacao=str(input("Qual sua nação fih! \n"))
if(idade >= 18 and sexo == "Masculino" and nacao == "Brasil"):
    print("Apto")
else:
    print("Não apto")