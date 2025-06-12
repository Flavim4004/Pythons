peso=float(input("Qual o seu peso fih! \n "))
altura=float(input("Qual sua altura fih! \n"))
imc=float(peso/(altura*altura))
ideal=float(21.75*(altura*altura))
if(imc <18.5):
    print("Voce esta abaixo do peso ideal logo a dieta recomendada e: \n 1.Consuma Gordura Saudavel \n 2.Proteina \n 3.carboidratos \n com o objetivo de aumentar seu peso \n")
    peso1=float(input("Voce quer \n [1]ganhar \n [2]perde \n peso fih? \n"))
    if(peso1 ==1 ):
        ganhar=(ideal-peso)
        print("Voce ganhou peso ficando \n " + str(ganhar))
    elif(peso1 == 2):
        perder=(peso-ideal)
        print("Voce perdeu peso ficando \n " + str(perder))
    else:
        print("PESO MANTIDO")
elif(imc>18.5 and imc <=24.9):
    print("Voce esta no peso ideal logo a dieta recomendada e: \n 1.Consuma Gordura Saudavel \n 2.Proteina \n 3.carboidratos \n com o objetivo de estabilizar seu peso \n")
    peso1=float(input("Voce quer \n [1]ganhar \n [2]perde \n peso fih? \n"))
    if(peso1 ==1 ):
        ganhar=(ideal-peso)
        print("Voce ganhou peso ficando \n " + str(ganhar))
    elif(peso1 == 2):
        perder=(peso-ideal)
        print("Voce perdeu peso ficando \n " + str(perder))
    else:
        print("PESO MANTIDO")
elif(imc > 24.9 and imc <=29.9):
    print("Voce esta com sobrepeso logo a dieta recomendada e: \n 1.Salada  \n 2.Evitar comidas gordurosas \n 3.Sucos e comidas naturais \n com o objetivo de estabilizar seu peso para o ideal")
    peso1=float(input("Voce quer \n  [1]ganhar \n [2]perde \n peso fih? \n"))
    if(peso1 ==1 ):
        ganhar=(ideal-peso)
        print("Voce ganhou peso ficando \n " + str(ganhar))
    elif(peso1 == 2):
        perder=(peso-ideal)
        print("Voce perdeu peso ficando \n " + str(perder))
    else:
        print("PESO MANTIDO")
elif(imc >29.9 and imc <=34.9):
    print("Voce esta com obesidade 1 logo a dieta recomendada e: \n 1.ir a um nutricionista ou proficional da area \n 2.Fazer exercícios fisicos \n 3.Evitar fast food \n ")
    peso1=float(input("Voce quer \n [1]ganhar \n [2]perde \n peso fih? \n"))
    if(peso1 ==1 ):
        ganhar=(ideal-peso)
        print("Voce ganhou peso ficando \n " + str(ganhar))
    elif(peso1 == 2):
        perder=(peso-ideal)
        print("Voce perdeu peso ficando \n " + str(perder))
    else:
        print("PESO MANTIDO")
elif(imc > 34.9 and imc < 40):
    print("Voce esra com obesidade 2 logo a dieta recomendada e: \n 1.Ir num medico urgentemente ou nutricionista \n 2.ir na academia \n 3.Participar de grupos de saude \n")
    peso1=float(input("Voce quer \n [1]ganhar \n [2]perde \n peso fih? \n"))
    if(peso1 ==1 ):
        ganhar=(ideal-peso)
        print("Voce ganhou peso ficando \n " + str(ganhar))
    elif(peso1 == 2):
        perder=(peso-ideal)
        print("Voce perdeu peso ficando \n " + str(perder))
    else:
        print("PESO MANTIDO")
elif(imc >+ 40 and imc <=50 ):
    print("Voce esta com obesidade 3 logo a dieta recomendada e: \n 1.Ir no nutricionista com melhor desmpenho da regiao \n 2.ir na melhor academia da regiao \n 3.Consultar especialistas \n ")
    peso1=float(input("Voce quer \n [1]ganhar \n [2]perde \n peso fih? \n"))
    if(peso1 ==1 ):
        ganhar=(ideal-peso)
        print("Voce ganhou peso ficando \n " + str(ganhar))
    elif(peso1 == 2):
        perder=(peso-ideal)
        print("Voce perdeu peso ficando \n " + str(perder))
    else:
        print("PESO MANTIDO")
elif(imc > 50):
    print("Voce esta com obesidade morbida logo a dieta recomendada e: \n 1.Procure ajuda imediantamente  \n 2.Participe dos killos mortais  \n 3.va a um nutricionista  \n")
    peso1=float(input("Voce quer \n [1]ganhar \n [2]perde \n peso fih? \n"))
    if(peso1 ==1 ):
        ganhar=(ideal-peso)
        print("Voce ganhou peso ficando \n " + str(ganhar))
    elif(peso1 == 2):
        perder=(peso-ideal)
        print("Voce perdeu peso ficando \n " + str(perder))
    else:
        print("PESO MANTIDO")