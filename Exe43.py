idade1=int(input("Qual sua idade fih? \n"))
idade2=int(input("Qual sua idade fih? \n"))
if(idade1 <= 9 and idade2 <=9):
    h=int(input("Que horas e a luta fih? \n"))
    print("Está marcado a luta de uma pessoa com " + str(idade1) + " anos e outra pessoa com " + str(idade2) + " anos na hora " + str(h) + "\n" )
elif(10 <= idade1 <= 14 and 10 <= idade2 <=14):
    h1=int(input("Que horas e a luta fih? \n"))
    print("Está marcado a luta de uma pessoa com " + str(idade1) + " anos e outra pessoa com " + str(idade2) + " anos na hora " + str(h1) + "\n" )
elif(15 <= idade1 <= 18 and 15 <= idade2 <=18):
    h2=int(input("Que horas e a luta fih? \n"))
    print("Está marcado a luta de uma pessoa com " + str(idade1) + " anos e outra pessoa com " + str(idade2) + " anos na hora " + str(h2) + "\n" )
elif(19 <= idade1 <=24 and 19<= idade2 <=24):
    h3=int(input("Que horas e a luta fih? \n"))
    print("Está marcado a luta de uma pessoa com " + str(idade1) + " anos e outra pessoa com " + str(idade2) + " anos na hora " + str(h3) + "\n" )
else:
    print("Luta cancelada!")