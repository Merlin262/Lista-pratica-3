varAu=0
varAu1=0

for i in range(10):
    num=int(input("Informe um numero: "))
    if (num%2==0):
        varAu=varAu+1
    else:
        varAu1=varAu1+1

#print(varAu)
#print(varAu1)

print("São " + str(varAu)  + " numeros pares e " + str(varAu1) + " numeros impares")
