n1=int(input("Digite um numero fih! \n"))
n2=int(input("Digite um numero fih! \n"))
resp=int(input("Escolha um calculo fih! \n [1]Soma \n [2]Subtração \n [3]Multiplicação \n [4]Divisão \n"))
match resp:
    case 1:
        soma=int(n1+n2)
        print("A soma é " + str(soma))
    case 2:
        sub=int(n1-n2)
        print("A subtração é " + str(sub))
    case 3:
        mult=int(n1*n2)
        print("A multiplicação é " + str(mult))
    case 4:
        div=int(n1/n2)
        print("A divisão é " + str(div))
    case _:
        print("Invalido fih")