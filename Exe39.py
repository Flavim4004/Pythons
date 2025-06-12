time=str(input("Escolha um time fih! \n"))
if(time == "Atletico"):
    uni1=int(input("Qual uniforme fih? \n 1[modelo 1] \n 2[modelo 2] \n"))
    if(uni1 == 1):
        print("o valor será de R$85,00")
    if(uni1 == 2):
        print("o valor será de R$75,00")
if(time == "Cruzeiro"):
    uni2=int(input("Qual uniforme fih? \n 1[modelo 1] \n 2[modelo 2] \n"))
    if(uni2 == 1):
        print("o valor será de R$45,00")
    if(uni2 == 2):
        print("o valor será de R$95,00")
else:
    print("Time cadastrado com sucesso")
