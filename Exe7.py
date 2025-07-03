n1=float(input("Digite um numero fih! \n"))
n2=float(input("Digite um numero fih! \n"))
n3=float(input("Digite um numero fih! \n"))
perg=int(input("Voce quer somar quias numeros fih? \n [1]Todos os 3 \n [2]o primeiro e o segundo \n [3]o segundo e o terceiro \n [4]o terceiro e o primeiro \n "))
match perg:
    case 1:
        soma=float(n1+n2+n3)
        print("A Soma é " + str(soma))
    case 2:
        soma1=float(n1+n2)
        print("A Soma é " + str(soma1))
    case 3:
        soma2=float(n2+n3)
        print("A Soma é " + str(soma2))
    case 4:
        soma3=float(n3+n1)
        print("A Soma é " + str(soma3))
    case _:
        print("Não existe")



    
