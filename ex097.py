a='Oi'
b='Todas as pessoas podem.'
c='Vidas vivas importam.'

def escreva(texto):
    z=len(texto)+5
    print('~'*z)
    print(f'  {texto:^}')
    print('~'*z)


escreva(a)
escreva(b)
escreva(c)