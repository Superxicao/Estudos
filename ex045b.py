import random
from time import sleep

itens=('Pedra','Papel','Tesoura')
maq=random.randint(0,2)
a='\033[7;1;33;40m'
b='\033[m'
c='\033[1;33;40m'
d='\033[36m'
e='\033[44m'
i='\033[42m'
j='\033[41m'
emp=f'{j}Empate!{b}'
vm=f'{j}Vitória da Máquina!{b}'
vj='{}Vitória do Jogador!{}'.format(j,b)


print(f'{d}=+={b}'*5,end='')
print("""
[0] PEDRA
[1] PAPEL
[2] TESOURA
""",end='')
print(f'{d}=+={b}'*5)

jog=(int(input(f'{c}Escolha sua jogada {b}{a};){b}')))

if jog in range(0,3):
    jogadas=f'{e}Você jogou {itens[jog]}e a máquina jogou {itens[maq]}.{b}'
    print(jogadas)
    if maq==0:
        if jog==0:
            print(emp)
        if jog==1:
            print(vj)
        if jog==2:
            print(vm)
    elif maq==1:
        if jog==0:
            print(vm)
        if jog==1:
            print(emp)
        if jog==2:
            print(vj)
    elif maq==2:
        if jog==0:
            print(vj)
        if jog==1:
            print(vm)
        if jog==2:
            print(emp)
else:
    print(f'{i}Jogada inválida{b}')