"""import random

num=random.randrange(0,5)
"""
from random import randint
from time import sleep

num=randint(0,5)
jog=int(input('Digite um numero de 0 a 5: '))
print('Procesando.......')
sleep(3)

if num==jog:
	print(num)
	print('Você ganhou! o número sorteado foi {}!'.format(num))
else:
	print('Você errou! O número sorteado foi {}. Tente novamente.'.format(num))
print('Fim do Jogo')