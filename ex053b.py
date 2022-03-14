#n=str(input('Escreva uma frase: '))
f='Todas as pessoas são felizes'

contrario=''
for x in range(len(f)-1,-1,-1):
    contrario+=f[x]
corte=contrario.split()
insere='*'.join(corte)
print(corte)
print(insere)
print(insere[::-1])
