alunos=list()
notas=list()
nota=list()
aluno=list()
temp=list()
c=0
while c<3:
    nome=str(input('Digite o nome do aluno: '))
    nota1=float(input('Digite a primeira nota: '))
    nota2=float(input('Digite a segunda nota: '))
    aluno.append(nome)
    nota.append(nota1)
    nota.append(nota2)
    notas.append(nota[:])
    aluno.append(notas[:])
    alunos.append(aluno[:])
    aluno.clear()
    nota.clear()
    notas.clear()
    print(alunos)
    c+=1

    p=''
    while p not in 'sn':
        p=str(input('Continuar? [s/n]: '))
    if p=='n':
        break

print('-='*30)
print('N°  Nome       Média')

for x in range(len(alunos)):
    for y in range(len(alunos[x])):
        for z in range(len(alunos[x][y])):
            print(alunos[x][y][z])
