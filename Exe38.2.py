nota=float(input("Quantos pontos voce tirou fih? \n"))
nota2=float(input("Quantos pontos voce tirou fih? 2 bim \n"))
nota3=float(input("Quantos pontos voce tirou fih? 3 bim \n"))
nota4=float(input("Quantos pontos voce tirou fih? 4 bim \n"))
soma=float(nota + nota2 + nota3 + nota4)
media=float(soma/4)
if(media >= 7):
    print("APROVADO!")
else:
    print("REPROVADO!")