pro=float(input("Quanto voce vai gastar com esse produto fih? \n "))
epoca=int(input("Em que epoca estamos fih? \n [1]Carnaval \n [2]Ferias \n [3]Dia das crianças \n [4]Black Friday \n [5]Natal \n"))
match epoca:
    case 1:
        pro1=float(pro+(pro*1.10))
        print("O preço no carnaval seria " + str(pro1))
    case 2:
        pro2=float(pro+(pro*1.20))
        print("O preço nas Ferias seria " + str(pro2))
    case 3:
        pro3=float(pro+(pro*1.05))
        print("O preço no dia das crianças seria " + str(pro3))
    case 4:
        pro4=float(pro-(pro*0.70))
        print("O preço na Black friday seria " + str(pro4))
    case 5:
        pro5=float(pro-(pro*0.95))
        print("O preço no Natal seria " + str(pro5))
    case _:
        print("Resposta invalida fih!")