from random import randint

jogador=jogadas=0
jogadasjogador=[]
maquina=randint(0,10)
print(maquina)

while jogador!=maquina:
    jogadas+=1
    jogador=int(input('Digite o número: '))
    jogadasjogador+=str(jogador)
#    if jogador in jogadasjogador:
#        jogador=int(input('Você já jogou esse número. Tente outro: '))
    if jogador==maquina:
        print('Você ganhou! O número escolhido pela máquina foi {} e você escolheu {}!\nE só precisou fazer {} jogadas!'.format(maquina,jogador,jogadas))
        print(jogadasjogador,len(jogadasjogador))