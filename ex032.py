from datetime import date

a=int(input('Digite o ano: '))

if a==0:
    a=date.today().year

print(a,'é um ano bissexto!' if a%4==0 and not a%100==0 or a%400==0 else 'não é ano bissexto!')
