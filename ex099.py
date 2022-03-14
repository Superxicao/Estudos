from random import randint

def maior(lista):
    maior=0
    for x in lista:
        if x>maior:
            maior=x
    print(f'O maior número da lista {lista} é o número {maior}.')

n=randint(0,10)
n2=[]

for x in range (n):
    n2.append(randint(0,100))

maior(n2)