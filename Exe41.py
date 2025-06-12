vendas=float(input("Quanto voce vendeu esse mes fih? \n"))
if(vendas >= 22000.00):
    tempo=int(input("A quanto tempo voce trabalha na empresa fih? \n 1.[menos de 2 anos] \n 2.[2 anos ] \n 3.[3 ou mais anos] \n" ))
    if(tempo == 1):
        cal1=float(vendas + (vendas * 0.02))
        print("A comissão fez seu salario ficar em " + str(cal1))
    if(tempo == 2):
        cal2=float(vendas + (vendas * 0.03))
        print("A comissão fez seu salario ficar em " + str(cal2))
    if(tempo == 3):
        cal3=float(vendas + (vendas * 0.04))
        print("A comissão fez seu salario ficar em " + str(cal3))
    else:
        print("Salario e o mesmo")
else:
    print("O salario e o mesmo")    