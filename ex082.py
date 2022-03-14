lista=[]
pares=[]
impares=[]

while True:
    n=int(input('Digite um número: '))
    lista.append(n)
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
    p='b'
    while p not in 'sn':
        p=str(input('Quer continuar? [S/N] ')).strip().lower()
    if 'n' in p:
        break

print(f'A lista ficou: {lista}, a de pares {pares} e a de impares {impares}.')


    