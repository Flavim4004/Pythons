cont=int(0)
cont1=int(0)
cont2=int(0)
cont10=int(0)
cont20=int(0)
cont50=int(0)
num=int(input("Quanto tu quer sacar fih! \n"))
while(num - 50 >= 0):
    cont50=cont50+1
    num=num-50
while(num - 20 >= 0):
    cont20=cont20+1
    num=num-20
while(num - 10  >= 0):
    cont10=cont10+1
    num=num-10
while(num - 2  >= 0 ):
    cont2=cont2+1
    num=num-2
while(num -1  >= 0):
    cont1=cont1+1
    num=num-1
print(f"{cont50} notas de 50 \n {cont20} notas de 20 \n {cont10} notas de 10 \n {cont2}  notas de 2 \n {cont1} notas de 1")

