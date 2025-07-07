cont=int(0)
somapar=int(0)
somaimpar=int(0)
par =[]
impar=[]
pergunta=[0,0,0,0]


for cont in range(0,4,1):
    pergunta[cont]=int(input("Digite um numero fih! \n"))
    if(pergunta[cont] %2 == 0):
        somapar=somapar+pergunta[cont]
        par.append(pergunta[cont])
    if(pergunta[cont] %2 == 1):
        somaimpar=somaimpar+pergunta[cont]
        impar.append(pergunta[cont])
print(f"{par}")
print(f"{impar}")
print(f"A soma dos pares é {somapar}")
print(f"A soma dos impares é {somaimpar}")