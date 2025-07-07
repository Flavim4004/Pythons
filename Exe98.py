maior=int(0)
menor=int(99999)
media=int(0)
soma=int(0)
cont=int(0)
cont1=int(0)
notas=[0,0,0,0,0,0]
for cont in range(0,6,1):
    notas[cont]=float(input("Digite uma nota fih! \n"))
    soma=soma+notas[cont]
    media=soma/6
    if(notas[cont] > maior):
        maior=notas[cont]
    if(notas[cont] < menor):
        menor=notas[cont]
    if(notas[cont] > media):
        cont1=cont1+1
print(f"A quantidade de notas acima da média é {cont1} \n A soma das notas é {soma} \n A média das notas é {media} \n A maior nota é {maior} \n A menor nota é {menor} ")
    

    