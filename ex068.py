from random import randint

c=vj=vm=0

print('\033[33mVamos jogar Par ou Ímpar!\033[m')
while True:
    maq=randint(0,10)
    
    j=str(input('Par ou Ímpar ou Sair? [P/I/S]: ').strip().lower()[0])
    while j not in 'pis':
        j=str(input('Responda corretamente. Par ou Ímpar ou Sair? ').strip().lower()[0])
    
    jog=int(input('Escolha um número de 1 à 10: '))
    while jog<1 or jog>10:
        jog=int(input('Digite um número válido: '))

    total=maq+jog
    resultado=total%2
    print('DEU PAR' if resultado==0 else 'DEU ÍMPAR')
    msg=f'Você jogou {jog}, a máquina jogou {maq}, total deu {total}.'
    if resultado==0:
        if j=='p':
            print('Você Venceu!',msg)
            vj+=1
        elif j=='i':
            print('Você perdeu.',msg)
            vm+=1
            break
    if resultado==1:
        if j=='p':
            print('Você perdeu.',msg)
            vm+=1
            break
        elif j=='i':
            print('Voce Ganhou!',msg)
            vj+=1
    elif jog=='s':
        break
    c+=1

print(f'Vezes que jogou: {c}\nPerdeu porque o total deu {total}.\nPlacar: Jogador {vj} x Máquina {vm}')