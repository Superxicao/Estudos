def volte():
    print('Volte Sempre!')

def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except Exception as erro:
            print(f'ERRO! Digite um número válido. Sobre o erro: {erro}')
        else:
            print(f'O número inteiro digitado foi {n}')
            break
    
def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except Exception as erro:
            print('Erro! Digite um número real válido. Sobre o erro: {}'.format(erro))
        else:
            print(f'O número real digitado foi {n:.2f}.')
            break

leiaint('Digite um número inteiro: ')
leiafloat('Digite um número real: ')
volte()