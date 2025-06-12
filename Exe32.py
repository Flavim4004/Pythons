idade1=int(input("Qual a sua idade fih? \n"))
idade2=int(input("Qual a sua idade fih? \n"))
idade3=int(input("Qual a sua idade fih? \n"))
idade4=int(input("Qual a sua idade fih? \n"))
menor=int(9999)
maior=int(0)
if(idade1 > maior):
    maior = idade1
if(idade1 < menor):
    menor = idade1
if(idade2 > maior):
    maior = idade2
if(idade2 < menor):
    menor=idade2
if(idade3 > maior):
    maior=idade3
if(idade3 < menor):
    menor = idade3
if(idade4 > maior):
    maior = idade4
if(idade4 < menor):
    menor = idade4
print("O maior numero é " + str(maior) + " ja o menor é " + str(menor))