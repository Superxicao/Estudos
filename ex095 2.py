jogador=dict()
jogadores=list()
gols=list()
somagols=0

while True:
    jogador['Nome']=str(input('Digite o nome do jogador: ')).strip()
    partidas=int(input('Quantas partidas ele jogou? '))
    for x in range(partidas):
        g=int(input('Quantos gols ele fez na {}° partida? '.format(x)))
        gols.append(g)
        somagols+=g
    
    jogador['Gols']=gols[:]
    gols.clear()
    jogador['Total']=somagols
    jogadores.append(jogador.copy())
    jogador.clear()
    continua=' '
    while continua not in 'sn':
        continua=str(input('Quer continuar? [S/N]: ')).lower()
    if continua in 'n':
        break

print('-='*30)
print(jogadores)
print('-='*30)
for i in jogadores[0].keys():
    print(f'{i:<15}',end='')
print()
print('-'*50)
print(f'{"N°":<3}')
for k,v in enumerate(jogadores):
    print(f'{k:<2}',end='')
    for d in v.values():
        print(f' {str(d):<13}',end=' ')
    print()

print('-'*50)

while True:
    while True:
        op=int(input('Digite o código do jogador (999 para finalizar): '))
        if op>len(jogadores)-1:
            print('OPÇÃO INVÁLIDA!!!!')
        elif op==999:
            break
        else:
            break
    if op==999:
        break
    if op>len(jogadores)-1 or op<0:
        print('Opção inválida.')

    print('=== Levantamento do jogador {} ===.'.format(jogadores[op]['Nome']))
    for i in range(len(jogadores[op]['Gols'])):
        print(f'    No {i+1}° jogo ele fez {jogadores[op]["Gols"][i]} gols.')
