altura=int(input('Digite a altura: '))
largura=int(input('Digite a largura: '))

area=largura*altura
tinta=area//2

print('A altura é {}m, a largura é {}m, a área é {}m², e serão necessários {} baldes de tinta para pintar a parede.'.format(altura,largura,area,tinta))