perg=int(input("O qual bom e o seu conheçimento em Excel fih? \n [1]Basico \n [2]intermediário \n [3]avançado \n"))
if(perg==1):
    resp1=int(input("Escolha uma formula fih! \n [1]SOMA \n [2]MÉDIA \n [3]MÁXIMO \n"))
    if(resp1==1):
        print("Soma todos os números em um intervalo de células")
    elif(resp1==2):
        print("Calcula a média aritmética dos números em um intervalo de células.")
    elif(resp1==3):
        print("Retorna o maior número em um intervalo de células.")
    else:
        print("Resposta invalida fih!")
elif(perg==2):
    resp2=int(input("Escolha uma formula fih! \n [1]SE \n [2]SOMASE \n [3]CONT.SE \n"))
    if(resp2==1):
        print("Executa um teste lógico e retorna um valor se a condição for VERDADEIRA e outro se for FALSA.")
    elif(resp2==2):
        print("Soma os valores em um intervalo que atendem a um determinado critério. ")
    elif(resp2==3):
        print("Conta o número de células em um intervalo que atendem a um determinado critério.")
    else:
        print("Resposta invalida fih!")
elif(perg==3):
    resp3=int(input("Escolha uma formula fih! \n [1]ORDEM.EQ \n [2]PRO.CV \n [3]PRO.CH \n"))
    if(resp3==1):
        print("Ordena os dados em um intervalo de células. Você precisa especificar se a ordenação é crescente ou decrescente e qual coluna usar como base para a ordenação.")
    elif(resp3==2):
        print("Procura um valor em uma coluna da esquerda de uma tabela e retorna um valor na mesma linha de outra coluna especificada.")
    elif(resp3==3):
        print("Similar ao PROCV, mas procura um valor em uma linha na parte superior de uma tabela e retorna um valor na mesma coluna de outra linha especificada.")
    else:
        print("Resposta invalida fih!")
else:
    print("ERRO! TENTE NOVAMENTE FIH!")