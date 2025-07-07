perg=int(input("Escolha um humorista fih! \n [1]Fabio Porchat \n [2] Danilo Gentili \n [3] Rafinha bastos \n "))
match perg:
    case 1:
        c=int(input("Qual cidade ele vai apresentar fih? \n [1]São Paulo \n [2]Araxa \n [3]Rio Grande do sul \n "))
        match c :
            case 1:
                print("Não tem show nessa cidade fih")
            case 2:
                idade=int(input("Qual sua idade fih? \n"))
                if(idade >= 18):
                    print("tem show do Fabio Porchat")
                else:
                    print("Tu é de menor fih! ")
            case 3:
                print("Não tem show nessa cidade fih!")
            case _:
                print("Resposta invalida!")                                
    case 2:
        ci=int(input("Qual cidade ele vai apresentar fih? \n [1]São Paulo \n [2]Araxa \n [3]Rio Grande do sul \n "))
        match ci:
            case 1:  
                  print("tem show do Danilo Gentili")   
            case 2:
                  print("Não tem show nessa cidade fih!")
            case 3:
                  print("Não tem show nessa cidade fih!") 
            case _:
                  print("Resposta invalida!")  
    case 3:
        cid=int(input("Qual cidade ele vai apresentar fih? \n [1]São Paulo \n [2]Araxa \n [3]Rio Grande do sul \n "))
        match cid:
             case 1:
                  print("Não tem show nessa cidade fih!")
             case 2:
                  print("Não tem show nessa cidade fih! ")
             case 3:
                  print("tem show do Rafinha bastos")
             case _:
                  print("Resposta invaida!")
    case _:
          print("Resposta invalida!")
                
                    
                         