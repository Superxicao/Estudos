pilha=[]
p=str(input('Digite a expressão: '))
for x in p:
    if x=='(':
        pilha.append(x)
    elif x==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha)>0:
    print('Expressão inválida.')
else:
    print('Expressão válida!')





while True:
    break