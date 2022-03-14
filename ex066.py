c=s=0

while True:
    n=int(input('Digite o {}° número: '.format(c+1)))
    if n==999:
        break
    s+=n
    c+=1

print(f'Você digitou {c} vezes e a soma deles é {s}.')