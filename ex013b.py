preco=float(input('Digite o valor do produto:' ))

desconto=preco-(preco*10/100)
print('Com desconto fica {} reais.'.format(desconto))
print('O valor parcelado totalizará {} reais'.format(preco+(preco*8/100)))

