cont=int(0)
contm=int(0)
contf=int(0)
contpes=int(0)
while(cont !=4):
    idade=int(input("Qual sua idade fih? \n"))
    sexo=int(input("Qual seu sexo fih \n [1]Masculino \n [2]Feminino \n"))
    cont=cont+1
    if(idade>=10):
        contpes=contpes+1
    if(sexo==1):
        contm=contm+1
    if(sexo==2 and idade <=20):
        contf=contf+1
print(f"Foram castradas \n {contpes} pessoas abaixo dos 10 anos, \n {contm} homens e \n {contf} mulheres abaixo dos 20 ")