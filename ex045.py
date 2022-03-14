import random
from time import sleep

n=random.randrange(1,4)
a='\033[7;1;33;40m'
c='\033[44m'
d='\033[1;46m'
e='\033[1m'
b='\033[m'

print("""{}{:=^50}{}""".format(a,'Jokenpô',b),"""
{}1: Pedra{}
{}2: Papel{}
{}3: Tesoura{}
""".format(e,b,e,b,e,b))

j=int(input('{}Faça sua jogada{}{};){}: '.format(c,b,a,b)))

if n==1:
    pc='Pedra'
elif n==2:
    pc='Papel'
elif n==3:
    pc='Tesoura'

if j==1:
    jog='Pedra'
elif j==2:
    jog='Papel'
elif j==3:
    jog='Tesoura'

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')


if n==1 and j==3 or n==2 and j==1 or n==3 and j==2:
    print('{}Você perdeu, você jogou {} e a máquina jogou!{}{}'.format(d,jog,pc,b))
elif j==1 and n==3 or j==2 and n==1 or j==3 and n==2:
    print('{}Você ganhou! Você jogou {} e a máquina jogou!{}{}'.format(d,jog,pc,b))
elif n==j:
    print('{}Você e a máquina empataram!!!{}'.format(d,b))
