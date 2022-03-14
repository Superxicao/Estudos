n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))

m=(n1+n2)/2
print('Sua média das notas {:.1f} e {:.1f} foi {:.1f}.'.format(n1,n2,m))

if m<5:
    print('\033[41mREPROVADO\033[m')
elif m>4.9 and m<7:
    print('\033[43mRECUPERAÇÃO\033[m')
elif m>=7 and m<=10:
    print('\033[44mAPROVADO\033[m')
