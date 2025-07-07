#Crie um programa que adicone times num vetor usando o .append
time=["atletico","Cruzeiro"]
for k in time:
    time.append(str(input("Digite o novo time fih! \n")))
    if(len(time)==4):
        break
print(time)