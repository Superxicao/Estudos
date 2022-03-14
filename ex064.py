c=-1
n=s=0

while n!=999:
    s+=n
    c+=1
    n=int(input('Digite um número: '))
    #if n!=999:
    #    s+=n
    
print('Você somou {} vezes e o resultado foi {}.'.format(c,s))