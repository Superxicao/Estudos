aluno=dict()
aluno['Nome']=str(input('Digite o nome do aluno: ')).strip()
aluno['Média']=float(input(f'Digite a média de {aluno["Nome"]}: '))

if aluno['Média']<5:
    aluno['Situação']='REPROVADO'
elif 5<=aluno['Média']<7:
    aluno['Situação']='RECUPERAÇÃO'
else:
    aluno['Situação']='APROVADO'

for i,e in aluno.items():
    print(f'{i} é igual a {e}.')