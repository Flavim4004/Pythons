cont=int(0)
contpeso1=int(0)
contpeso2=int(0)
contp3=int(0)
contp4=int(0)
while(cont != 4):
    a=int(input("Qual seu sexo fih? \n [1]Masculino \n [2]Feminino \n"))
    b=float(input("Qual seu peso fih? \n"))
    if(a == 1 and b <= 78.5):
        contpeso1=contpeso1+1
    elif(a == 1 and b >78.5):
        contpeso2=contpeso2+1
    elif(a == 2 and b <=59.6):
        contp3=contp3+1
    elif(a== 2 and b  > 59.6):
        contp4=contp4+1
    else:
        print("")
    cont=cont+1
print(f"Homens abaixo do peso medio {contpeso1} \n Homens acima do peso médio {contpeso2} \n Mulheres abaixo do peso medio {contp3} \n Mulheres acima do peso medio {contp4} \n")