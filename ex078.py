n=[]
m=[]
M=[]
a=maior=menor=0
while a<4:
    n.append(int(input('Digite um número: ')))
    if n[a]>maior:
        maior=n[a]
        pos=a
        M.append(a)
    if menor==0 or n[a]<=menor:
        menor=n[a]
        m.append(a)
    a+=1

print("""A lista foi: {}.
O maior número foi {} na posição {}.
O menor número foi {} na posição {}.
""".format(n,maior,pos,menor,m))

print(f'O maior número foi {maior} na posição ',end='')
for x in M:
    print(x,end=' ')
print(f'\nO menor número foi {menor} na posição ',end='')
for x in m:
    print(menor,end=' ')
print('\nA lista em For fica: ',end='')
for x in n:
    print(x,end=' ')

print(f'\nO número maior {maior} aparece com enumerate em: ',end='')
for posicao,elemento in enumerate(n):
    if elemento==maior:
        print(posicao,end=' ')

print(f'\nO número menor {menor} aparece com enumerate em: ',end='')
for posicao,elemento in enumerate(n):
    if elemento==menor:
        print(posicao,end=' ')

print(f'\nO número maior {maior} de outra forma aparece em: ',end='')
cont=0
for elemento in n:
    if elemento==maior:
        print(cont,end=' ')
    cont+=1

print(f'\nO número menor {menor} de outra forma aparece em: ',end='')
cont=0
for elemento in n:
    if elemento==menor:
        print(cont,end=' ')
    cont+=1

print(f'organizado fica: {sorted(n)}')