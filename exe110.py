import exe110funcoes
a=int(input("Digite um valor fih! \n"))
b=int(input("Digite um valor fih! \n"))
peg=int(input("Escolha uma formula fih! \n [1]Adição \n [2]Subtração \n [3]Multiplicação \n [4]Divisão \n"))
if(peg == 1):
    exe110funcoes.soma(a,b)
elif(peg == 2):
    exe110funcoes.subtracao(a,b)
elif(peg == 3):
    exe110funcoes.multiplicacao(a,b)
elif(peg == 4):
    exe110funcoes.dvisao(a,b)