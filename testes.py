from os import system

f=1
while (f==1):
    try:
        n=int(input('Digite o número: '))
        n2=int(input('Digite o divisor: '))
        n3=n%n2
        print(n3)
        if n==f:
            f==0
    except (TypeError())
        print('Digite um número válido')

system('pause')