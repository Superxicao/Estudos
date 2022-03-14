P=p=0
for x in range(5):
    p1=float(input('Digite o peso em kg: '))
    print(p1)
    if p1>P:
        P=p1
        print(P)
    if p==0:
        p=p1
    if p>p1:
        p=p1

print('{} e {}'.format(P,p))

