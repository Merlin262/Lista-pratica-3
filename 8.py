num=int(input("Informe um número: "))

if num>0:
    for i in range(1,num):
        if num%i==0:
            print(i)
        