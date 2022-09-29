qtd=int(input("Informe a quantidade de idades: "))
varAu=0
for i in range(qtd):
    idade=int(input("Informe a idade: "))
    varAu=idade+varAu

print(varAu/qtd)