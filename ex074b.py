from random import randint

n=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Os números sorteados foram:',end=' ')
for a in n:
    b=print(a,end=' ')
print(f'\nO maior número foi {max(n)} e o menor foi {min(n)}')
