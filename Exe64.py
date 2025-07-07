cont=int(0)
five=int(0)
tree=int(0)
while(cont != 7):
    cont=cont+1
    if(cont %3 == 0):
        tree=tree+1
    elif(cont %5 == 0):
        five=five+1
print(f"Foram identificados {five} números que são múltiplos de cinco e {tree} números que são multiplo por 3.")