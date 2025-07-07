cont=int(0)
soma=int(0)
for cont in range(0,200,1):
    num=int(input("Digite um numero fih! \n"))
    soma=soma+num
    if(soma >1000):
        exe=soma-1000
        break
    if(soma == 1000):
        break
print(f"excedeu em {exe}")
