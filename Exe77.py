cont=int(0)
num=int(input("Digite um numero para ver a tabuada fih! \n"))
for cont in range(0,11,1):
    total=int(num*cont)
    print(f"{num}x{cont}={total}")