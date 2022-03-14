from random import randint

n=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
maior=menor=0
print(n)
for a in n:
    if a>maior:
        maior=a
    if menor==0 or a<menor:
        menor=a

print(f'O maior é o {maior} e o menor é {menor}')
