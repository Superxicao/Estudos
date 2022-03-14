import moeda

v=float(input('Digite o valor: '))
print("""A metade de {:.2f} é {:.2f}.
O dobro de {:.2f} é {:.2f}.
Aumentado em 10% fica {:.2f}.
Diminuido em 10% fica {:.2f}.
""".format(v,moeda.metade(v),v,moeda.dobro(v),moeda.aumentar(v,10),moeda.diminuir(v,10)))
