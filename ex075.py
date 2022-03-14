n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
n3=int(input('Digite mais um número: '))
n4=int(input('Digite o último número: '))

t=(n1,n2,n3,n4)

if t.count(3)!=0:
    index=t.count(3)
else:
    index='nenhuma.'

f=' vezes.' if t.count(9)>1 or t.count(9)==0 else ' vez.'
print(f'Você digitou os valores {t}.\n'
       f'O valor 9 apareceu {t.count(9)}{f}\n'
       f'O valor 3 foi digitado pela 1° vez na posição {index}\n'
       'Os números pares foram:',end=' ')

for a in t:
    if a%2==0:
        print(a,end=' ')
    
if 3 in t:
    print(f'\nO valor 3 foi digitado pela 1° vez na posição {t.index(3)}')
else:
    print('\nO valor 3 não foi digitado.')