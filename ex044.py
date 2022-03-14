print('\033[44m{:=^40}\033[m'.format('LOJAS XICOWS'))
p=float(input('Digite o valor do produto: '))

c='\033[41m'
d='\033[m'
g='\033[44m'
h='\033[1;7;33;41m'
i='\033[45m'

print(c,'{:=^40}'.format('Escolha uma opção'),d)
print("""
{}1: À vista, dinheiro/cheque;{}
{}2: À vista, cartão;{}
{}3: Em até duas vezes no cartão;{}
{}4: 3x à 20x no cartão;{}
""".format(c,d,c,d,c,d,c,d),end='')

o=int(input('{}Digite a opção: {}'.format('\033[1m',d)))

if o==1:
    preco=p-p*10/100
    print('{}O preço do produto que custa R${:.2f} reais.\nÀ vista no dinheiro ou cheque fica em R${:.2f} reais com 10% de desconto{}'.format(g,p,preco,d))
elif o==2:
    preco=p-p*5/100
    print('{}O preço do produto que custa R${:.2f} reais.\nÀ vista no cartão fica em R${:.2f} reais com 5% de desconto.{}'.format(g,p,preco,d))
elif o==3:
    print('{}O preço do produto dividido no cartão em 2x permanece em R${:.2f} reais.{}'.format(g,p,d))
elif o==4:
    preco=p+p*20/100
    vezes=int(input('{}Quantas parcelas? {}'.format(g,d)))
    parc=preco/vezes
    print('{}O preço do produto que custa R${:.2f} reais.\nParcelado em mais de 3x fica em R${:.2f} reais com 20% de juros.{}'.format(g,p,preco,d))
    if vezes>20:
        print(f'{h}NEGADO{d}')
    else:
        print('{}O valor das parcelas ficará em {} vezes de R${:.2f} reais.{}'.format(i,vezes,parc,d))
else:
    print(f'{i}OPÇÃO INVÁLIDA{d}')

    