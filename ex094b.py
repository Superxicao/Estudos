pessoal=[]

"""[{'Nome': 'dano', 'Sexo': 'm', 'Idade': 76},
{'Nome': 'maro', 'Sexo': 'm', 'Idade': 32},
{'Nome': 'lara', 'Sexo': 'f', 'Idade': 43}]
"""
pessoa=dict()
media=idades=0

while True:
    pessoa['Nome']=str(input('Nome: ')).strip()
    while True:
        pessoa['Sexo']=str(input('Sexo (f/m): ')).strip().lower()
        if pessoa['Sexo'] in 'fm':
            break
        print('ERRO. TENTE NOVAMENTE.')
    pessoa['Idade']=int(input('Idade: '))
    pessoal.append(pessoa.copy())
    while True:
        p=str(input('Quer continuar? [s/n]: ')).lower()
        if p in 'sn':
            break
        print('DIGITE UMA OPÇÃO VÁLIDA.')
    if p in 'n':
        break

for x in pessoal:
    idades+=x['Idade']

media=idades/len(pessoal)

print(f"""Temos {len(pessoal)} pessoas cadastradas.
A média de idade é de {media}
As mulheres cadastradas foram:""",end=' ')
for x in pessoal:
    for k,v in x.items():
        if v=='f':
            print(x['Nome'],end=' ')
print('Os mais velhos são:')
for x in pessoal:
    if x['Idade']>media:
        for k,v in x.items():
            print(f'{k} = {v};',end=' ')
        
"""
print(pessoal)
for x in pessoal:
    for k,v in x.items():
        print(k,v)
        if k=='Sexo':
            print(' aquiiii ',x)
"""