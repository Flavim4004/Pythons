cont=int(0)
numero=[3,6,12,24,48,96,192,384,768,1536]
for k in numero:
    if(k == 3 or k == 6 or k == 96):
        print(f"${k}$")
    else:
        print(k)
print("------------------------------------")
numero1=[3,0,0,0,0,0,0,0,0,0,0,0,0]
for cont in range(0,10,1):
    numero1[cont+1]=numero[cont]*2
    if(numero1[cont]==3 or numero1[cont]==6 or numero1[cont] == 96):
        print(f"${numero1[cont]}$")
    print(numero1[cont])
