from random import randint
from time import sleep

numeros=[]
jogos=[]
vezes=int(input('Quantas jogos você quer que eu sugira? '))
c=0
while c<vezes:
    d=0
    while d<6:
        num=randint(0,60)
        if num not in numeros:
            numeros.append(num)
            d+=1
    print(f'{c}°: [{numeros}]')
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    c+=1

for x,y in enumerate(jogos):
    print(f'Jogo {x+1}: {y}')
    sleep(0.5)