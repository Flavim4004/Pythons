carro=float(input("Quantos kms voce rodou fih?"))
dias=float(input("Quanos dias essa viagem ta fih?"))
cal1=float(dias * 60.0)
cal2=float(carro*0.15)
total=float(cal1 + cal2)
print("O preço total do carro alugado é " + str(total))