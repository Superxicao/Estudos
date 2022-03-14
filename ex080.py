lista=[]

for x in range(10):
    n=int(input('Digite um número: '))
    if x==0 or n>lista[-1]:
        lista.append(n)
        print('Inserido na última posição.')
    else:            
        pos=0
        while pos<len(lista):
            if n<=lista[pos]:
                lista.insert(pos,n)
                print(f'Inserido na posição {pos}.')
                break
            pos+=1

print(lista)















"""lista=[]
maior=menor=c=pos=0

for x in range(5):
    n=int(input('Digite um número: '))
    maior=pos=0
    for a in range(len(lista)):
        if lista[a]<=n and lista[a]>maior:
            maior=lista[a]
            pos=a

    print(lista)
    print(f'o maior antes do {n} é {maior}')

    if lista==[] or pos==(len(lista)):
        lista.append(n)
        print('Foi inserido no final da lista.')
    else:
        lista.insert(pos,n)
        print(f'O valor foi inserido na posição {pos}.')
    c+=1

print(f'Os valores digitados foram {lista}')
        
        
if lista[x]>=maior and lista[x]<=n:
            menor=lista[x]
            print(f'O maior mais próximo de {n} é o {menor}')
        if lista[x]<=maior and lista[x]>=n:
            maior=lista[x]
            print(f'O menor de todos e maior que o {n} é o {maior}')

#aqui tenho as posições em que oss valores devem entrár na lista
for x in lista:
        if x<n and x>=maior:
            maior=x
        if x>n:
            maiordecima=x
            if maiordecima<=menor:
                menor=x

print(f'O maior antes do {n} é o {maior}')
print(f'O menor depois do {n} é o {menor}')


verificação do menor a partir do valor, mas mostrou-se desnecessária
                if x>n:
            maiordecima=x
            if maiordecima<=menor:
                menor=x
                p2=a
"""