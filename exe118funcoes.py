def posto(venda,escolha):
    if(escolha == 1 and venda <=20):
        g=float(2.50)
        cal1=g*venda
        cal2=float(cal1-(cal1*0.04))
        return cal2
    elif(escolha == 1 and venda >20):
        g=float(2.50)
        cal1=g*venda
        cal2=float(cal1-(cal1*0.06))
        return cal2
    elif(escolha == 2 and venda <=20):
        a=float(1.90)
        cal1=a*venda
        cal2=float(cal1-(cal1*0.03))
        return cal2
    elif(escolha ==2 and venda >20):
        a=float(1.90)
        cal1=a*venda
        cal2=float(cal1-(cal1*0.06))
        return cal2