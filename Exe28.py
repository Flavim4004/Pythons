v=float(input("qual velocidade voce esta fih? \n"))
m=450+(10*(v -80))
if(v <= 80):
    print("Velocidade segura")
else:
    print("A Multa e de 450 mais os km a mais fica " + str(m))