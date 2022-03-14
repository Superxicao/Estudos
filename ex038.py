n1=int(input('\033[45mDigite o primeiro número: \033[m'))
n2=int(input('\033[45mDigite o segundo número: \033[m'))

if n1>n2:
    print(f'\033[1;33mO primeiro número, número {n1}, é maior.\033[m')
elif n1==n2:
    print(f'\033[45mOs númeos {n1} e {n2} são iguais!\033[m')
else:
    print(f'\033[1;33mO segundo número, número {n2}, é maior.\033[m')