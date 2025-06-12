peso=float(input("Qual seu peso no planeta terra fih? \n "))
p=int(input("Escolha um planeta para conversão de peso fih \n [1]Mercurio \n [2]Venus \n [3]Marte \n [4]Jupter \n [5]Saturno \n [6]Urano \n"))
match p:
    case 1:
        m1=(peso+(peso*0.37))
        print("Seu peso em Mercurio Seria " + str(m1))
    case 2:
        m2=(peso+(peso*0.88))
        print("Seu peso em Venus seria " + str(m2))
    case 3:
        m3=(peso+(peso *0.38))
        print("Seu peso em Marte seria " + str(m3))
    case 4:
        m4=(peso+(peso*2.64))
        print("Seu peso em Jupter seria " + str(m4))
    case 5:
        m5=(peso+(peso*1.15))
        print("Seu peso  em  Saturno seria " + str(m5))
    case 6:
        m6=(peso+(peso*1.17))
        print("Seu peso em Urano seria "+ str(m6))
    case _:
        print("RESPOSTA INVALIDA FIH!")
