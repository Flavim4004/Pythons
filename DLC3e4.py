cont=int(0)
soma=float(0.0)
contp=int(0)
v=[]
for cont in range(0,999999,1):
    compra=float(input("Quanto voc vai gastar nessa compra fih! \n"))
    v.append(compra)
    soma=soma+compra
    contp=contp+1
    print(f"Os preços dos produtos adioionados ate o momento é:{v} \n A soma dos produtos é: {soma} \n Sua quantidade é:{contp} \n ")
    para=int(input("Voce quer para fih! \n [1]Sim [2]Não \n"))
    if(para == 1):
        break
    else:
        print("")
pagamento=int(input("Qual a forma de pagamento fih! \n [1]Vista [2]Boleto [3]Credito \n"))
if(pagamento==1):
    cal=soma*0.90
elif(pagamento ==2):
    cal=soma*1.10
elif(pagamento == 3):
    cal=soma*0.95
print(f"O preço ficou {cal}")