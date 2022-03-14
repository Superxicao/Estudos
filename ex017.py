import math
co=int(input('Digite o valor do cateto oposto: '))
ca=int(input('Digite o valor do cateto adjacente: '))

a=pow(co,2)+pow(ca,2)
hip=math.sqrt(a)

print('A hipotenusa é {}cm.'.format(hip))