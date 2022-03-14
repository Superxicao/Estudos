p=float(input('Escreva seu peso: ' ))
a=float(input('Escreva sua altura: '))

imc=p/a**2
print(f'Seu imc é de {imc:.1f}')
if imc<18.5:
    print('ABAIXO DO PESO')
elif imc<=25:
    print('PESO IDEAL')
elif imc<=30:
    print('SOBREPESO')
elif imc<=40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
