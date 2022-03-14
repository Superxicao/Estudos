from time import sleep

def contador(i,f,p):
    if p<0:
        p=-1
    if p==0:
        p=1
    if i<=f:
        while i<=f:
            print(i,end=' ',flush=True)
            sleep(0.5)
            i+=p
        print('Fim!')
    else:
        while i>=f:
            print(i,end=' ',flush=True)
            sleep(0.5)
            i-=p
        print('Fim!')
contador(1,10,1)
contador(10,0,2)

inicio=int(input('Início: '))
fim=int(input('Fim: '))
passo=int(input('Passo: '))

contador(inicio,fim,passo)