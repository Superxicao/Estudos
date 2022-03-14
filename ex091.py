from random import randint
from operator import itemgetter

jogadores={'Jogador1':randint(1,6),
           'Jogador2':randint(1,6),
           'Jogador3':randint(1,6),
           'Jogador4':randint(1,6)}
print('VALORES SORTEADOS')

for k,v in jogadores.items():
    print(f'\033[44mO {k} sorteou {v}.\033[m')
ranking=sorted(jogadores.items(),key=itemgetter(1),reverse=True)

for i,v in ranking:
    print(f'{i} sorteou: {v}')

for i,v in enumerate(ranking):
    print('{:^4}° lugar: {:<10} sorteou: {:>3}'.format(i+1,v[0],v[1]))
