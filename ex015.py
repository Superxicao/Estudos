dis=int(input('Digite os Km percorridos: '))
dias=int(input('Digite por quantos dias: '))

custo=dias*60
gas=dis*0.15
total=custo+gas

print('O custo total foi de {} reais.'.format(total))