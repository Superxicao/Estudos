n=str(input('Digite o nome todo: '))

ver=n.lower().find('silva')
print(ver)
ver2=n.lower()
print('silva' in n)
n2=n.lower()
ver3=n2.find('silva')
print(ver3)
print('Opção 4: {}'.format('silva' in n2))

n=str(input('Digite o nome todo: '))
print('Seu nome tem Silva? {}'.format('silva' in n.lower()))