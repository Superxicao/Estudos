f=int(input('Digite o número: '))
fat=1

while f>0:
    print(f,end='')
    fat*=f
    print(end=' x ' if f>1 else ' = ')
    f-=1

print(fat)
