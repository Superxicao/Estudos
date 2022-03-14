lista=(('Lápis',1.75),('Borracha',2.00),('Caderno',15.90),('Estojo',25.00),
('Transferidor',4.20),('Compasso',9.99),('Mochila',120.32),('Canetas',22.30),
('Livro',34.90))

for a in lista:
    #print(a)
    print(f'{a[0]:.<30}R$',f'{a[1]:>8}')

a=0

while True:
    #print(f'{lista[a][0],lista[a][1]}')
    print(f'{lista[a][0]:.<30}R${lista[a][1]:>8}')
    if a==len(lista)-1:
        break
    a+=1
