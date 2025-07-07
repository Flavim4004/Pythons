def cobrar(km,dias):
    cal1=int(dias*60)
    cal2=float(km*0.15)
    cal3=float(cal1+cal2)
    print(f"O carro percorreu {km} kms em {dias} dias dando um total de {cal3}")