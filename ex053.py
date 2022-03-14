n=str(input('Vamos analisar: ').strip().lower())

contrario=n[::-1]
contrario2=''
for x in range(len(n)-1,-1,-1):
    print(x,end=' ')
    contrario2+=n[x]
print(len(n), contrario)

if n==contrario2:
    print('Palíndromo!')
else:
    print('Não é palíndromo!')




#"""n=str(input('Vamos analisar: ').strip().upper())
#contrario=''
#for l in range(len(n)-1,-1,-1):
#    contrario+=n[l]
#
#print(contrario,n,contrario==n)
#
#contrario2=n[::-1]
#print(contrario2)"""