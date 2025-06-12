resp=int(input("Qual serie voce viu esse final de semana fih! \n [1]Rick and morty \n [2]Dungeon Meshi \n [3]Star Wars Andor  \n "))
match resp :
    case 1:
        print("Rick and morty ")
    case 2:
        print("Dungeon Meshi")
    case 3:
        print("Star wars Andor")
    case _:
        print("E uma otima escolha ")