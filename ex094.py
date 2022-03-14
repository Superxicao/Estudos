cadastro=dict()
cadastrados=list()
maisvelhos=list()
idades=media=mulheres=c=0

while True:
    cadastro['Nome']=str(input('Nome: ')).strip()
    cadastro['Sexo']=' '
    while True:
        cadastro['Sexo']=str(input('Sexo [M/F]: ')).lower().strip()
        if cadastro['Sexo'] in 'fm':
            break
        else:
            print('Digite somente "M" ou "F".',end=' ')
    cadastro['Idade']=int(input('idade: '))
    cadastrados.append(cadastro.copy())
    p=' '
    while True:
        p=str(input('Quer continuar? [s/n]: '))
        if p not in 'sn':
            print('Opção inválida.',end=' ')
        else:
            break
    if p=='n':
       break

for i in cadastrados:
    for v,m in i.items():
        if v=='Idade':
            idades+=m
            if m>40:
                maisvelhos.append(i.copy())
        if m=='f':
            mulheres+=1
        
media=idades/len(cadastrados)

print('A) Ao todo tem {}'.format(len(cadastrados)),'pessoa cadastrada.' if len(cadastrados)==1 else 'pessoas cadastradas')
print("""B) A média de idade é de {:.0f}.
C) As mulheres cadastrasdas são: {}.
D) Lista de pessoas que estão acima da média: \n{}""".format(media,mulheres,maisvelhos))

for i,v in enumerate(maisvelhos):
    print(i,v)

print('\n\n',cadastrados)