cont=int(0)
soma=int(0)
somapar=int(0)
somainpar=int(0)
contpar=int(0)
continpar=int(0)
for cont in range(0,4,1):
    num=int(input("Digite um numero fih! \n"))
    soma=soma+num
    if(num %2==0):
        contpar=contpar+1
        somapar=somapar+num
    elif(num %2==1):
        continpar=continpar+1
        somainpar=somainpar+1
print(f"Foram cadastrados {contpar} números pares \n Foram cadastrados {continpar} números inpares \n A soma dos pares é {somapar} \n A soma dos inpares é {somainpar} \n A soma geral é {soma} \n ")