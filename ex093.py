jogador=dict()

jogador['Nome']=str(input('Nome do jogador: ')).strip()
jogador['Partidas']=int(input('Partidas que ele jogou: '))
jogador['Gols']=[]
gols=0

for x in range(jogador['Partidas']):
    jogador['Gols'].append(int(input('Quantos gols na {}° partida? '.format(x+1))))
    gols+=jogador['Gols'][x]

for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}.')

print(jogador)
print('O jogador {} jogou {} partidas.'.format(jogador['Nome'],jogador['Partidas']))

for i in range(len(jogador['Gols'])):
    print(f'Fez {jogador["Gols"][i]} gols na {i+1}° partida.')
print('Fez um total de {} gols.'.format(gols))

"""a forma de somar intems de uma tupla é sum(nomedatupla)"""