import random
v=[1,3,7,10]
s=v[random.randint(0,3)]

num=int(input("Digite um numero de 1 a 10 fih! \n"))
if(num == s):
    soma=s+num
    print(f"A soma é {soma}")
else:
    print("errooouuu")