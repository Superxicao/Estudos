import random

a1=str(input('Digite o nome 1: '))
a2=str(input('Digite o nome 2: '))
a3=str(input('Digite o nome 3: '))
a4=str(input('Digite o nome 4: '))

alunos=[a1, a2, a3, a4]
ordem=random.shuffle(alunos)
print('A ordem dos alunos é:\n{}'.format(alunos))