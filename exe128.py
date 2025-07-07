import random
import exe128funcoes
cal1=float(0)
cal2=float(0)
cont=int(0)
v=[0,0,0,0]
for cont in range(0,4,1):
    v[cont]=random.randint(1,4)
    exe128funcoes.analise_3(v)
    
r=exe128funcoes.analise_3(v[3])
t=exe128funcoes.analise_2(v[2])
soma=float(r+t)
mult=float(soma*3.14)
print(f"O sorteio deu {v} e o dobro do 3 valor deu {r} o trio do 2 valor deu {t} a soma dos dois é {soma} e sua multiplicação fica {mult} ")


