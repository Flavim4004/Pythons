per1=str(input("Seu perssonagem e velho? \n"))
per2=str(input("Seu perssonagem e do mal? \n"))
per3=str(input("seu perssonagem luta com espada a laizer? \n"))
per4=str(input("Seu perssonagem é esperto? \n"))
per5=str(input("Seu perssonagem apareceu em uma animação? \n "))
andor=int(0)
darth=int(0)
yoda=int(0)
if(per1== "sim"):
    darth=darth + 1
    yoda=yoda + 1
else:
    andor = andor + 1
if(per2 == "sim"):
    darth = darth + 1
else:
    yoda = yoda +1
    andor = andor + 1
if(per3 == "sim"):
    yoda = yoda + 1
    darth = darth + 1
else:
    andor = andor + 1
if(per4 == "sim"):
    andor = andor + 1
    darth = darth + 1
    yoda = yoda + 1
if(per5 == "sim"):
    darth = darth + 1
    yoda = yoda + 1
else:
    andor = andor + 1
print("O Darth vader ficou com " + str(darth) + " pontos \n ja o yoda ficou com " + str(yoda) + " pontos \n e o Andor ficou com " + str(andor) + " pontos")

