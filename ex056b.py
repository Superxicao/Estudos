nomemaisvelho=''
idademaisvelho=0
mulheresnovas=0
media=0

for x in range(4):
    nome=str(input('Nome: ').strip())
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: '))
    media+=idade
    if sexo in 'Mm' and idade>idademaisvelho:
        idademaisvelho=idade
        nomemaisvelho=nome
    if sexo in 'Ff' and idade<20:
        mulheresnovas+=1

print("""A média de idade do grupo é de {} anos.
O membro mais velho é o {} e tem {} anos.
Há {} mulheres abaixo de 20 anos no grupo.
""".format(media//4,nomemaisvelho,idademaisvelho,mulheresnovas))