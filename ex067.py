c=0

while True:
    n=int(input('Digite o número para a tabuada: '))
    print('=-='*4)
    if n<0:
        break
    for x in range(1,11):
        print(f'{n:<2} x {x:>2} = {n*x}')
    print('=-='*4)
    c+=1

print(f'{c} tabuadas feitas.')