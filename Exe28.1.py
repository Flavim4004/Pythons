v=float(input("Qual sua velocidade fih?"))
if(v <= 80):
    print("Velocidade segura fih")
if(v >= 81 and v <=100):
    cal1=150+(5*(v-80))
    print("A multa sera de " + str(cal1))
elif(v>= 101 and v <= 160):
    cal2=250+(10*(v-80))
    print("A multa sera de " + str(cal2))
elif(v>=161 and v <=230):
    cal3=500+(20*(v-80))
    print("A multa sera de " + str(cal3))
else:
    print("O veiculo sera confiscado fih!")

