total=int(input('Quanto você quer sacar? '))

ced=50
totced=0

while True:
    if total>=ced:
        total-=ced
        totced+=1
        #print('t=',total,end=' ')
    else:
        if totced>0:
            print(f'Serão {totced} notas de {ced}.')
            #print(total,totced,end=' ')
        if total>=20:
            ced=20
        elif total>=10:
            ced=10
        elif total>=1:
            ced=1
        if total==0:
            break
        totced=0