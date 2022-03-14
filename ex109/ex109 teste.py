import moeda

v=float(input('Digite o valor: '))
print(f'A metade de {moeda.moeda(v)} é {moeda.metade(v,True)}.')
print(f'O dobro de {moeda.moeda(v)} é {moeda.dobro(v,True)}.')
print(f'Aumentado em 10% fica {moeda.aumentar(v,10,True)}.')
print(f'Diminuido em 10% fica {moeda.diminuir(v,10,True)}.')