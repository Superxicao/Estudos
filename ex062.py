p=int(input('Primeiro termo: '))
r=int(input('Razão: '))
contador=min=0
max=10
mais=max

while mais!=0:
    while min<max:
        print(p,end=' ')
        p=p+r
        contador+=1
        min+=1
    mais=int(input('\nQuantos mais? '))
    if mais>0:
        max=mais
        min=0

print('Você fez {} operações.'.format(contador))