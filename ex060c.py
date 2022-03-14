f=int(input('Digite o número: '))

print(f'{f}! = ',end='')
for x in range(f-1,0,-1):
    print(x,end=' x ' if x>1 else ' = ')
    f*=x
print(f)