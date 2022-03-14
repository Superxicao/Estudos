p=int(input('Primeiro termo: '))
r=int(input('Razão: '))
contador=cont=0
mais=max=10
while mais!=0:
    while cont<max:
        print(p,end=' ')
        p=p+r
        cont+=1
        contador+=1
    mais=int(input('\nQuer mais vezes? '))
    max+=mais

print('Você fez {} operações.'.format(contador))

    