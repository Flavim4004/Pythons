def investigar(a,b,c,d,e):
    contsus=int(0)
    if(a == 1):
        contsus=contsus+1   
    if(b == 1):
        contsus=contsus+1
    if(c == 1):
        contsus=contsus+1
    if(d == 1):
        contsus=contsus+1
    if(e ==1):
        contsus=contsus+1
    if(contsus < 2):
        print("Inocente")
    if(contsus ==2):
        print("Suspeito")
    if(contsus >=3 and contsus <=4):
        print("Cumplice")
    if(contsus ==5):
        print("Assasino")
             