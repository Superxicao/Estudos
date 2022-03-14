n=int(input('Digite um número: '))
cont=0
for x in range(1,n+1):
    if n%x==0:
        print('\033[33m',end=' ')
        cont+=1
    else:
        print('\033[31m',end=' ')
    print(x,end='\033[m')

print('\nO número foi dividido {} vezes.'.format(cont),end=' ')

if cont==2:
    print('É primo!')
else:
    print('Não é primo!')


"""
n=int(input('Digite o número: '))

for x in range(2,n):
    if n%x==0:
        print('Não é primo.')
        break
else:
    print('É primo.')"""