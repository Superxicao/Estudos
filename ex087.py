n=[[],[],[]]
somapares=somaterceiracoluna=maiorsegundalinha=0

for x in range(3):
    for y in range(3):
        n[x].append(int(input(f'Digite o número [{x},{y}]: ')))
        
for x in range(3):
    for y in range(3):
        print(f'[{n[x][y]:^5}]',end='')
    print('')

for x in range(len(n)):
    for y in range(3):
        if n[x][y]%2==0:
            somapares+=n[x][y]
        if n[1][y]>maiorsegundalinha:
            maiorsegundalinha=n[1][y]
    if n[x][2]:
        somaterceiracoluna+=n[x][2]

print(f'''A soma dos pares é {somapares}.
A soma dos valores da terceira coluna é {somaterceiracoluna}.
O maior valor da segunda linha é {maiorsegundalinha}.''')