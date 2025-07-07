cont=int(0)
contm=int(0)
for cont in range(0,3,1):
    nome=str(input("Qual seu nome fih? \n"))
    sexo=int(input("Qual seu sexo fih? \n [1]Homen \n [2]Mulher \n"))
    if(sexo== 1):
        contm=contm+1
print(f"foram cadastrados {contm} Homens ")