print(f'{"-"*40}')
print(f'{"LISTA DE PREÇOS":^40}')
print(f'{"-"*40}')

lista=('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,
'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)

for a in range(len(lista)):
    if a==0 or a%2==0:
        print(f'{lista[a]:.<30}R${lista[a+1]:>8}')

print(f'{"-"*40}')

for a in range(0,len(lista),2):
    print(f'{lista[a]:.<30}R${lista[a+1]:>8}')

for a in lista:
    if type(a) is str:
        print(f'{a:.<30}R$',end='')
    else: #if type(a) is float:
        print(f'{a:>8}')