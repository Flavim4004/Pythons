def lascado(div,tempo,taxa):
    juros=int(div*tempo*taxa)
    total=div+juros
    print(f"Os juros foram {juros} ja o total é {total}")
