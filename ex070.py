precoalto=precobarato=total=cont=0

while True:
    produto=str(input('Nome do produto: ')).strip()
    preco=float(input('Preço: '))

    total+=preco
    if preco>1000:
        precoalto+=1
    if precobarato==0 or preco>precobarato:
        precobarato=preco
        maisbarato=produto
  
    cont+=1
    continua='c'
    while continua not in 'sn':
        continua=str(input('Mais produtos? [S/N]')).strip().lower()[0]
    if continua=='n':
        break
    
print("""Total: R${:.2f}.
{} produtos custam mais de R$1000.00.
O home do produto mais barato é {}
Você comprou {} produtos.""".format(total,precoalto,maisbarato,cont))