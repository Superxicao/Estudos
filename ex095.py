jogador=dict()
gols=list()
somagols=0

while True:
    jogador['Nome']=str(input('Digite o nome do jogador: ')).strip()
    partidas=int(input('Quantas partidas ele jogou? '))
    for x in range(partidas):
        g=int(input('Quantos gols ele fez na {}° partida? '.format(x)))
        gols.append(g)
    jogador['Gols']=gols[:]
    gols.clear()
    continua=' '
    while continua not in 'sn':
        continua=str(input('Quer continuar? [S/N]: ')).lower()
    if continua in 'n':
        break

for x in jogador['Gols']:
    somagols+=x
jogador['Total']=somagols

print('-='*30)
print(jogador)
print('-='*30)

for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v};')

print('-=*'*30)
print('O jogador {} jogou {} partidas:'.format(jogador['Nome'],partidas))
for i,v in enumerate(jogador['Gols']):
    print('Na partida {} ele fez {} gols.'.format(i+1,v))
