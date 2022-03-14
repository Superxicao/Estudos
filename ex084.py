n=[]
pessoas=[]

while True:
    n.append(str(input('Nome: ')).strip().lower())
    n.append(float(input('Peso: ')))
    pessoas.append(n[:])
    n.clear()
    q='m'
    maior=menor=x=0
    maispesados=[]
    maisleves=[]
    while x<len(pessoas):
        if pessoas[x][1]>maior:
            maior=pessoas[x][1]
            maispesados.append(pessoas[x])
        if x==0 or pessoas[x][1]<menor:
            menor=pessoas[x][1]
            maisleves.append(pessoas[x])
        x+=1

    if q not in 'sn':
        q=str(input('Quer continiar? s/n: ')).strip().lower()
    if q=='n':
        break

print(f'''Foram cadastradas {len(pessoas)} pessoas.
Os mais pesados são {maispesados}.
Os mais leves são {maisleves}.
''')

for x in pessoas:
    if x[1]==maior:
        print(f'Mais pesada: {x[1]}')
    if x[1]==menor:
        print(f'Mais leve: {x[1]}')
