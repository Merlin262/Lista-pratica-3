lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
valores=[]
repetidos=set()

for lista in lista:
    if lista not in valores:
        valores.append(lista)
    else:
        repetidos.add(lista)

print(repetidos)