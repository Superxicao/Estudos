from datetime import date

an=int(input('Digite o ano do nascimento: '))
a=date.today().year
c=a-an

print('O aluno tem {} anos.'.format(c))
if c<=9:
    print('MIRIM')
elif c>9 and c<=14:
    print('INFANTIL')
elif c>14 and c<=19:
    print('JUNIOR')
elif c>19 and c<=25:
    print('SENIOR')
elif c>25:
    print('MASTER')