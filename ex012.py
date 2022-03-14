preco=float(input('Digite o preço: '))

desconto=preco-preco*0.5
#desconto=preco-(preco*5/100)

print('O preço é: {:.2f} reais\nCom desconto fica {:.2f} reais'.format(preco,desconto))