c=0
lista=[]
lista2=[]
pares=[]
impares=[]
while c<7:
    n=int(input('Digite o número: '))
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
    c+=1
lista.append(pares[:])
lista.append(impares[:])
lista[0].sort()
lista[1].sort()
print(lista)