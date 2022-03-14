a=float(input('Digite a medida da primeira reta: '))
b=float(input('Digite a medida da segunda reta: '))
c=float(input('Digite a medida da terceira reta: '))

if a+b>c and b+c>a and a+c>b:
    print('Podem formar um triânglo!')
else:
    print('Não podem formar um triângulo!')