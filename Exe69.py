cont=int(0)
multa=int(1)
while(cont !=9999):
    usuario=str(input("Qual seu usuario fih? \n"))
    senha=str(input("Qual sua senha fih? \n "))
    if(usuario == "facil" and senha == "ff"):
        print("Login efetuado com sucesso \n")
        break
    else:
        multa*=2
        print(f"Voce errou logo sera multado em {multa} ")
    dnv=int(input("gostaria de tentar dnv fih? \n [1]Sim \n [2]Não \n "))
    if(dnv == 2):
        break
