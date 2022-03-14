valor=int(input('Digite o valor que quer sacar: '))

n50=valor//50
n20=(valor%50)//20
n10=(valor%20)//10
n1=(valor%10)
if n50!=0:
    print(f'Notas de 50: {n50:>2}')
if n20!=0:
    print(f'Notas de 20: {n20:>2}')
if n10!=0:
    print(f'Notas de 10: {n10:>2}')
if n1!=0:
    print(f'Notas de 1: {n1:>3}')


"""
if valor%50>0:
    n50=valor//50
    n20=valor%50
    print(f'{n50} notas de 50.')
if n20%20>0:
    n20//=20
    n10=n20%20
    print(f'{n20} notas de 20.')
if n10%10>0:
    n10//=10
    n1=n10%10
    print(f'{n10} notas de 10.')
if valor%1>0:
    print(f'{n1} notas de 1.')
"""