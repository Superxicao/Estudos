n=[[],[],[],[],[],[],[],[],[]]

for x in range(3):
    for y in range(3):
        n[x].append(int(input(f'Digite o número para [{x},{y}]: ')))

for x in range(3):
    for y in range(3):
        print(f'( {n[x][y]} )',end=' ')
        if y==2:
            print('')

print(n)


