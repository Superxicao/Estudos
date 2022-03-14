n=str(input('Digite o nome completo: '))

M=n.upper()
m=n.lower()

tamanho1=len(n.replace(' ',''))

replace2=n.replace(' ','')
tamanho2=len(replace2)

fatia=n.split()
insercao=''.join(fatia)
tamanho3=len(insercao)

tamanhoPrimeiroNome=len(n[0])

print("""
Maiúsculas: {}
Minúsculas: {}
Tamanho 1: {}
Tamanho 2: {}
Tamanho 3: {}


""".format(M,m,tamanho1,tamanho2,tamanho3))


"""
n=str(input('Digite o nome: ')).strip()

print('Maiúsculas: {}'.format(n.upper()))
print('Minúsculas: {}'.format(n.lower()))
print('Letras: {}'.format(len(n)-n.count(' ')))
print('Primeiro nome: {}'.format(n.find(' ')))"""