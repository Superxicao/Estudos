f=int(input('Digite o número: '))
fat=1
while f!=0:
    print(f'{f}',end='')
    fat+=fat*(f-1)
    f=f-1
    print(end=' x ' if f>0 else ' = ')
print(fat)