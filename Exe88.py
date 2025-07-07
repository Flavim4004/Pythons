cont=int(0)
contm=int(0)
for cont in range(0,5,1):
    nome=str(input("Digite seu nome fih! \n"))
    if(nome == "Marcos"):
        contm=contm+1
    else:
        print("")
print(f"Foram {contm} pessoas com o nome Marcos \n")