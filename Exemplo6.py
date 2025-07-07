#arrays -> vetor
#inteiro a[4] = {"joaquim","22","rua a","40"}
a = ["Joaquin",22,"rua a",40]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
a.append("Pedro")
print(a[4])
print("-------------------------")
cont= int(0)
for cont in range(0,5,1):
    print(a[cont],end="")
    #soma=soma+a[cont]
print("--------------------------")
for k in a:
    #iterar o vetor
    print(k)
    #soma = soma + k
#métodos ->São rotinas que pertecem a um elemento


