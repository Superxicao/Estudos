n=[[0,0,0],[0,0,0],[0,0,0]]

for x in range(3):
    for y in range(3):
        n[x]=int(input(f'Digite um número para casa [{x},{y}]: '))
for x in range(3):
    for y in range(3):
        print(f'[{n[x]:^5}]',end='')
    print('')


