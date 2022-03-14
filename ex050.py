s=cont=0
for c in range(1,7):
    n=int(input(f'Digite o {c}º número: '))
    if n%2==0:
        s+=n
        cont+=1
print('Você digitou {} números pares que somados dão {}.'.format(cont,s))