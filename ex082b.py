lista=[]
pares=[]
impares=[]

while True:
    lista.append(int(input('Digite um número: ')))
    p=' '
    while p not in 'sn':
        p=str(input('Quer continuar? [S/N] ')).strip().lower()
    if p in 'n':
        break

c=0
while c<len(lista):
    if lista[c]%2==0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
    c+=1 

print('lista: {}, pares {}, impares {}.'.format(lista,pares,impares))