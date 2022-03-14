a=str('-+'*20)
v=str('\033[42m')
v2=str('\033[32m')
f=str('\033[m')

print("""\033[41m{}\033[m
\033[33mEscolha uma opção:\033[m
{}1: Binário;{}
{}2: Octal;{}
{}3: Hexadecimal;{}
\033[41m{}{}
""".format(a,v,f,v,f,v,f,a,f),end='')

n=int(input('{}Digite um número: {}'.format(v2,f)))
o=int(input('{}Digite a opção desejada: {}'.format('\033[32m','\033[m')))

if o==1:
    print('O número {} em binário é: {}'.format(n,bin(n)[2:]))
elif o==2:
    print('O número {} em octal é: {}'.format(n,oct(n)[2:]))
elif o==3:
    print('o número {} em hexadecial é: {}'.format(n,hex(n)[2:]))