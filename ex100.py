from random import randint
numeros=[]
pares=[]
somadospares=[]

def sorteio():
    numeros.clear()
    for x in range(5):
        n=randint(0,100)
        numeros.append(n)
    print('Os números sorteados foram {}.'.format(numeros))

def somapar():
    soma=0
    for x in numeros:
        if x%2==0:
            soma+=x
            pares.append(x)
    somadospares.append(soma)
    print('A soma dos pares {} deu {}.'.format(pares,somadospares))

sorteio()
somapar()