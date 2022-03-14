from random import randint
from time import sleep

def somapar(lista):
    soma=0
    print('Os números pares são:',end=' ')
    for x in lista:
        if x%2==0:
            sleep(0.3)
            print(x,end=' ',flush=True)
            soma+=x
    print('e a soma dos pares é {}.'.format(soma))

def crianumeros(lista):
    print('Os números sorteados são:',end=' ',flush=True)
    for x in range(5):
        sleep(0.3)
        n=randint(0,100)
        print(f'{n} ',end='',flush=True)
        lista.append(n)
    print('FIM')

numeros=list()

crianumeros(numeros)
somapar(numeros)


