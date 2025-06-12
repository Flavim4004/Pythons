dis=float(input("Quantos km rodamos fih? \n"))
if(dis <= 200):
    cal1=float(0.35 * dis)
    print("O preço da viagem ficou " + str(cal1) + "\n")
if(dis > 200):
    cal2=float(0.20*dis)
    print("O preço da viagem ficou " + str(cal2) + "\n")
per=str(input("O bairro e perigoso fih? \n "))
if(per == "sim" and dis <= 200):
    cal3=float(dis*0.35*2)
    print("O preço da viagem ficou " + str(cal3) + "\n")
elif(per == "sim" and dis > 200):
    cal4=float(dis*1.8*0.20)
    print("O preço da viagem ficou " + str(cal4) + "\n")


