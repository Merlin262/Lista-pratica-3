num=0
valor=int(input("Ïnforme um valor: "))

if valor>0 and valor<11:
    for num in range(11):
        print(num*valor)