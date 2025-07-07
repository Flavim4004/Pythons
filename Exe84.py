cont=int(0)
contid=int(0)
contnm=int(0)
for cont in range(1,99999,1):
    nome=str(input("Digite seu nome fih! \n"))
    idade=int(input("Digite sua idade fih? \n"))
    if(idade != 35):
        contid=contid+1
    if(nome != "João"):
        contnm=contnm+1
    if(cont >3):
        print("BLOQUEADO! \n")
        break
    elif(nome == "João" and idade == 35):
        print("Cadastrado com sucesso! \n")
        break
print(f"Tentativas: \n nomes errados:{contnm} \n idades erradas:{contid}")