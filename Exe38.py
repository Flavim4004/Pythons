res1=int(input("Qual o valor da casa fih? \n"))
res2=int(input("Qual o seu salario fih? \n"))
res3=int(input("quanto tempo voce vai financiar a casa fih? \n"))
por1=int(res2*30)
por2=float(por1/100)
parcela= res1/res3
if(por2 > parcela):
    print("Emprestimo cancelado! \n")
else:
    print("O valor de " + str(res2) + " foi inserido com sucesso \n ")
