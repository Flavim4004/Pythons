def analise(valor,pag):
    if(pag == 1):
        valor*0.9
        print(f"O valor ficou {valor}")
    if(pag == 2):
        valor*1.1
        print(f"O valor ficou {valor}")
    if(pag == 3):
        parcelas=int(input("Quantas Parcelas fih! \n"))
        cal1=int(valor*1.20)
        cal2=cal1/parcelas
        print(f"O valor com as parcelas ficou {cal2}")

    