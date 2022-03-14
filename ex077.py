lista=('aprender','programar','linguagem','python','curso','gratis',
'estudar','praticar','trabalhar','mercado','programador','futuro')

for a in lista:
    print('\nNa palavra',a.upper(),'temos as vogais',end=' ')
    for b in a:
        if b in 'aeiou':
            print(b,end=' ')