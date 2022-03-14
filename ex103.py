def ficha(n='<desconhecido>',g=0):
    print(f'O jogador {n} fez {g} gols.')

nome=str(input('Digite o nome do Jogador: ')).strip()
gols=str(input('Quantos gols ele fez? '))

if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome=='':
    ficha(g=gols)
else:
    ficha(nome,gols)
