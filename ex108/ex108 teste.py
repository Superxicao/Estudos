import moeda

v=float(input('Digite o valor: '))
print(f'A metade de {moeda.moeda(v)} é {moeda.moeda((moeda.metade(v)))}.')
print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}.')
print(f'Aumentado em 10% fica {moeda.moeda(moeda.aumentar(v,10))}.')
print(f'Diminuido em 10% fica {moeda.moeda(moeda.diminuir(v,10))}.')
