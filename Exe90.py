cont=int(0)
somapar=int(0)
contpar=int(0)
for cont in range(0,6,1):
    num=int(input("Digite um numero fih! \n"))
    if(num %2==0):
        somapar=somapar+num
        contpar=contpar+1
print(f"A soma dos pares é {somapar} \n A contagem dos pares é {contpar}")
