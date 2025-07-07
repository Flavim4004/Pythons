cont=int(0)
conth=int(0)
for cont in range(0,3,1):
    nome=str(input("Digite um nome fih! \n "))
    sexo=int(input("Qual seu sexo fih? \n [1]Masculino \n [2]Feminino \n "))
    if(sexo == 1):
        conth=conth+1
    elif(sexo == 2):
        print("")
print(f"Foram cadastrados {conth} homes ")
