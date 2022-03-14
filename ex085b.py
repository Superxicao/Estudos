c=0
n=[]
pares=[]
impares=[]
lista=[]
while c<7:
    n.append(int(input('Digite o número: ')))
    c+=1

for x in range(len(n)):
    if n[x]%2==0:
        pares.append(n[x])
    else:
        impares.append(n[x])

        
#    else:
 #       if n[x]<=impares[x] or impares[x]==[]:
  #          pares.insert(x,n)

lista.append(pares)
lista.append(impares)
print(lista)