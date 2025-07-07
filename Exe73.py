import random as r

cont=(0)
soma=(0)
while(cont != 9999):
    s=r.randint(1,9)
    num=int(input("Digite um numero fih!\n"))
    gra=int(input("A soma do numero e: \n [1]Par \n ou \n [2]Impar \n"))
    soma=s+num
    resultado = 0

    if(soma % 2 == 0): resultado = 1
    else: resultado = 2

    if(gra == resultado):
        print("Ganhou fih!!! \n")
        print(f"O numero era {soma}")
        break
    else:
        print("Perdeu na hakari bet!!! \n")
        print(f"O numero era {soma}")
        break    


