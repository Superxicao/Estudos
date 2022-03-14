numeros=('zero','um','dois','tres','quatro','cinco',
        'seis','sete','oito','nove','dez','onze','doze',
        'treze','quztorze','quinze','dezesseis','dezessete',
        'dezoiteo','dezenove','vinte')

while True:
    n=int(input('Digite um número: '))
    if 0<=n<=20:
        print(f'O número escohido foi {numeros[n]}')
        r='a'
        while r not in 'sn':
            r=str(input('Quer continuar: [S/N]'.lower()))
            if r=='n':
                break
