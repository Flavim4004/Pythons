import exe116funcoes
divida=int(input("Voce ta devendo fih! \n [1]Sim [2]Não \n "))
if(divida == 1):
    div=int(input("Qual a divida fih! \n"))
    tempo=int(input("Quanto tempo voce esta com essa divida fih! \n"))
    taxa=int(input("Qual a taxa fih? \n"))
    exe116funcoes.lascado(div,tempo,taxa)
if(divida == 2):
    print("Então ta bom")

