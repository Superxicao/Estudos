from time import sleep

numeros=[]

def Maior(*n):
    maior=0
    print('Analisando os valores...',flush=True)
    sleep(1)
    for x in n:
        if x>maior:
            maior=x
        numeros.append(x)
    print('O maior número dentre os números {} é o {}.'.format(numeros,maior))

Maior(4,6,9,8,10)