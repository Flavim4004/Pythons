peso=float(input("Qual seu peso na terra fih? \n"))
per=int(input("Voce quer ver seu peso em: \n [1]Mercurio \n [2]Venus \n [3]Marte \n [4]Jupter \n [5]Saturno \n [6]Urano \n" ))
if(per==1):
    cal1=(peso*0.37)
    print("Seu peso seria " + str(cal1))
elif(per==2):
    cal2=(peso*0.88)
    print("Seu peso seria " + str(cal2))
elif(per==3):
    cal3=(peso*0,38)
    print("Seu peso seria " + str(cal3))
elif(per==4):
    cal4=(peso*2.64)
    print("Seu peso seria " + str(cal4))
elif(per==5):
    cal5=(peso*1.15)
    print("Seu peso seria " + str(cal5))
elif(per==6):
    cal6=(peso*1.17)
    print("Seu peso seria " + str(cal6))
else:
    print("Seu peso seria " + str(peso))