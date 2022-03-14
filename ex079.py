c=0
lista=[]
while True:
    p='v'
    while True:
        n=int(input('Digite um número: '))
        if n not in lista:
            lista.append(n)
            break
        else:
            print('Este número já está na lista.')
    while p not in 'sn':
        p=str(input('Quer continuar? [S/N]? ').strip().lower())
    if p=='n':
        break
    
print(sorted(lista))
lista.sort()
print(lista)

