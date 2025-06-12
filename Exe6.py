peg=int(input("Qual e o seu conhecimento no excel fih! \n [1]Basico \n [2]Intermediario \n [3]Avançado \n"))
match peg:
    case 1:
        bas=int(input("Escolha uma formula fih! \n [1]SOMA \n [2]MÉDIA \n [3]MÁXIMO \n"))
        match bas:
            case 1:
                print("Soma todos os números em um intervalo de células.")
            case 2:
                print(" Calcula a média aritmética dos números em um intervalo de células. ")
            case 3:
                print("Retorna o maior número em um intervalo de células.")
            case _:
                print("INVALIDO!")
    case 2:
        ite=int(input("Escolha uma formula fih! \n [1]SE \n [2]SOMASE \n [3]CONTSE \n"))
        match ite:
            case 1:
                print("Executa um teste lógico e retorna um valor se a condição for VERDADEIRA e outro se for FALSA.")
            case 2:
                print("Soma os valores em um intervalo que atendem a um determinado critério.")
            case 3:
                print("Conta o número de células em um intervalo que atendem a um determinado critério.")
            case _:
                print("INVALIDO!")
    case 3:
        ava=int(input("EScolha uma formula fih! \n [1]ORDEM.EQ \n [2]PRO.CV \n [3]PRO.CH \n "))
        match ava:
            case 1:
                print("Ordena os dados em um intervalo de células. Você precisa especificar se a ordenação é crescente ou decrescente e qual coluna usar como base para a ordenação. ")
            case 2:
                print("Procura um valor em uma coluna da esquerda de uma tabela e retorna um valor na mesma linha de outra coluna especificada.")
            case 3:
                print("Similar ao PROCV, mas procura um valor em uma linha na parte superior de uma tabela e retorna um valor na mesma coluna de outra linha especificada.")
            case _:
                print("INVALIDO!")
    case _:
        print("INVALIDO!")
                