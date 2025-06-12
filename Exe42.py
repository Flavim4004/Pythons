nota1=float(input("Qual sua nota fih? \n"))
nota2=float(input("Qual sua nota fih? 2 bim. \n"))
fre=float(input("Qual a sau frequencia fih? \n"))
freq=float(fre/100)
freq2=float(freq*75)
soma=float(nota1 + nota2)
media=float(soma/2)
if(media >60 and fre > freq2):
    print("Aprovado \n")
elif(media >=40 and media <=60 ):
    rec=float(input("Qual a nota de recuperação fih? \n"))
    if(rec <= 69.99):
        print("Reprovado fih \n")
elif(media <= 39.9):
    print("reprovado fih \n")