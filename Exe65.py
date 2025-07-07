cont=int(0)
maior=int(0)
menor=int(999)
conth=int(0)
contm=int(0)

nomeF = ""
nomeM = ""

while(cont != 5):
    nome=str(input("Qual seu nome fih? \n"))
    idade=int(input("Qual sua idade fih? \n"))
    sexo=int(input("Qual seu sexo fih? \n [1]Masculino \n [2]Feminino \n"))
    cont=cont+1
    if(idade < menor and sexo == 2):
        menor=idade
        contm=contm+1
        nomeF = nome
    if(idade > maior and sexo == 1):
        maior=idade
        conth=conth+1
        nomeM = nome
print(f"O homem '{nomeM}' mais velho tem {maior} anos ja a mulher '{nomeF}' mais nova tem {menor} anos ")    