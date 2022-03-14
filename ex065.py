run='s'
maior=menor=media=cont=0
while run in 'Ss':
    n=int(input('Digite um número: '))
    if n>maior:
        maior=n
    if menor==0:
        menor=n
    if menor>n:
        menor=n
    cont+=1
    media+=n
    run=str(input('Quer continuar [S/N]? '))
    if run not in 'SsNn':
        run=str(input('Digite apenas [S/N]: '))
print('A média entre os valores é {:.2f};\nO maior foi {} e o menor foi {}.\nVocê digitou {} valores.'.format(media/cont,maior,menor,cont))