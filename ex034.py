s=float(input('Digite o salário: '))

if s>1250:
    a=s+(s*10/100)
    t='10%'
else:
    a=s+(s*15/100)
    t='15%'

print('O seu salário de {:.2f} reais aumentará para {:.2f} reais, sofreu um aumento de {}.'.format(s,a,t))