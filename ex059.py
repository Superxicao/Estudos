n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
#menu=True
op=soma=multiplica=maior=0

while op!=5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair""")
    op=int(input('Escolha o que quer fazer: '))
    if op==1:
        soma=n1+n2
        print('A soma de {} com {} é: {}'.format(n1,n2,soma))
    elif op==2:
        multiplica=n1*n2
        print('A multiplicação entre {} e {} é {}.'.format(n1,n2,multiplica))
    elif op==3:
        maior=n1 if n1>n2 else n2
        print('Entre {} e {} o maior é {}.'.format(n1,n2,maior))
    elif op==4:
        n1=int(input('Digite outro número: '))
        n2=int(input('Digite mais outro número: '))
    else:
        op=int(input('Digite uma opção válida: '))

"""if op>5 or op<1:
        op=int(input('Escolha uma opção válida: '))
    elif op==5:
        menu=False
    """