cont=int(0)
valor=int(input("Qual o valor da compra fih! \n"))
pag=int(input("Digite uma forma de pagamento fih! \n [1]Vista ou pix \n [2]Cartão de Debito \n [3]cartão de credito em parcelas \n"))
if(pag == 1):
    cal1=valor-(valor*0.10)
    print(f"O total ficou {cal1}")
elif(pag == 2):
    cal2=valor-(valor*0.05)
    print(f"O total ficou {cal2}")
elif(pag ==3):
    taxa=int(input("Quantas parcelas voce quer pagar fih! \n"))
    if(taxa <= 3):
        par1=(valor/taxa)
        par2=par1+(par1*0.05)
        print(f"sua compra de {valor} parcelada em {taxa} de {par1}  sendo um total de {par2}")
    elif(taxa >3):
        par3=(valor/taxa)
        par4=par3+(par3*0.10)
        print(f"sua compra de {valor} parcelada em {taxa} de {par3}  sendo um total de {par4}")