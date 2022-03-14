def leiaint(n):
    while True:
        teste=str(input(n))
        if teste.isnumeric():
            break
        else:
            print('\033[31mERRO! DIGITE UM NÚMERO VÁLIDO.\033[m')
    return teste


num=leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
