tamanho=float(input("Qual tamanho da casa 1 fih? \n"))
lata=int(0)
while(tamanho > 0):
    lata = lata + 1
    tamanho = tamanho - 108
valor= lata * 80
print(f"Falta pintar {tamanho} e gatei {lata} latas e o valor é {valor} ")
print("-----------------------------------------------------------------")
tamanho=float(input("Qual tamanho da casa 2 fih? \n"))
galao=int(0)
galao = galao + 1
tamanho=tamanho-21.60
valor=galao*25
print(f"Falta pintar {tamanho} e gatei {galao} galao e o valor é {valor} ")
print("------------------------------------------------------------------")
tamanho=float(input("Qual tamanho da casa 3 fih? \n"))
lata=int(0)
galao=int(0)
while(tamanho >=108):
    lata=lata+1
    tamanho=tamanho-108
while(tamanho >=0):
    galao=galao+1
    tamanho=tamanho-21.6
valor=(lata*80)+(galao*25)
print(f"Vou gastar {lata} de latas é {galao} de galoes ficando {valor}")

