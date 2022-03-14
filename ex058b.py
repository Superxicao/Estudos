from random import randint

acertou=False
jogadas=0
maq=randint(1,10)
print('Sorteei um número de 1 a 10. Adivinhe!')

while not acertou:
    jogador=int(input('Digite o número:'))
    jogadas+=1
    if jogador==maq:
        print('Você ganhou!')
        acertou=True
    else:
        if jogador>maq:
            print('Menos...')
        else:
            print('Mais...')

print('Em {} jogadas você acertou o número {} que sorteei!'.format(jogadas,jogador))