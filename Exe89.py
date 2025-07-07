cont=int(0)
div=int(1)
num=int(input("Digite um numero fih \n"))
while(div <= num ):
    if(num %div==0):
        cont=cont+1
    div=div+1
if(cont == 2):
    print("Primo!")
else:
    print("Não e primo")