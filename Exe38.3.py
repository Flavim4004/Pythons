valor=float(input("Digite um valor fih? \n" ))
paga=int(input("Qual a forma de pagamento fih? \n 1. dinheiro ou pix \n 2.A vista no cartão \n 3.duas parcelas \n 4.tres ou mais parcelas \n" ))
if(paga == 1):
    cal1=float(valor -(valor * 0.15))
    print("O novo preço é " + str(cal1))
if(paga ==2):
    cal2=float(valor -(valor * 0.15 ) )
    print("O novo preço é " + str(cal2))
if(paga == 3):
    print(" o Preço não mudou ficando " + str(valor))
if(paga == 4):
    par=int(input("Quantas parcelas fih? \n"))
    cal3=float(valor/par)
    cal4=float(cal3 +(cal3*0.1))
    print("Voce parcelou em " + str(par) + " logo o preço do produto ficou " + str(cal4))