nome=str(input('Digite o nome: '))
media=float(input('Digite a média: '))
situacao='Reprovado' if media<7 else 'Aprovado'
alunos={'Nome':nome,'Média':media,'Situação':situacao}

for i,e in alunos.items():
    print(f'{i} é igual a {e}.')

