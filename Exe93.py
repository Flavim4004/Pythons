cont=int(0)
fran=float(1.50)
sara=float(1.10)
while(cont != 999):
    cont=cont+1
    
    sara=sara+0.03
    fran=fran+0.02
    if(sara > fran):
        break
print(f"Foram necessarios {cont} para sara ser maior que francisco")