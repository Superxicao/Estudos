s=a=0
for i in range(1,501,2):
    if i%3==0:
        s+=i
        a+=1
print(f'{s} é a soma dos números ímpares múltiplos de 3.\n{a} números.')