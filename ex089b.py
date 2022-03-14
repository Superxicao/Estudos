ficha=[]

while True:
    nome=str(input('Digite o nome do aluno: ')).strip()
    nota1=float(input('Digite a nota do aluno: '))
    nota2=float(input('Digite a outra nota do aluno: '))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    continua=' '
    while continua not in 'sn':
        continua=str(input('Quer continuar? [s/n]')).strip().lower()
    if continua=='n':
        break

print('-='*10)
print(f'{"N°":<3}{"Nome":<10}{"Média":>3}')
for i,a in enumerate(ficha):
    print(f'{i:<3}{a[0]:<10}{a[2]:>3.1f}')
print('-='*10)

while True:
    opc=int(input('Digite qual aluno você quer ver as notas: '))
    if opc<(len(ficha)):
        print(f'Aluno: {ficha[opc][0]:<10}; Notas: {ficha[opc][1]}')
    continua=' '
    while continua not in 'sn':
        continua=str(input('Quer continuar? [s/n]: ')).strip().lower()
    if continua=='n':
        break