from time import sleep

def contador(i,f,p):
    for x in range(i,f,p):
        print(x,end=' ',flush=True)
        sleep(0.6)
    print('FIM')

for x in range(10):
    print(x,end=' ',flush=True)
    sleep(0.6)
print('FIM!')
print('=-'*30)

for x in range(10,-1,-2):
    print(x,end=' ', flush=True)
    print(0.6)
print('FIM!')
print('-='*30)

inicio=int(input('Digite o início: '))
fim=int(input('Digite o fim: '))
passo=int(input('Digite o passo: '))

contador(inicio,fim,passo)