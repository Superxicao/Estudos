nomes=[]
idades=0
media=mulheresjovens=maisvelho=0
nomemaisvelho=''

for x in range(4):
    nome=str(input('Nome: '))
    idade=int(input('idade: '))
    sexo=str(input('sexo[M/F]: ').strip().lower())
    nomes+=nome
    idades+=idade
    if sexo=='f' and idade<20:
        mulheresjovens+=1
    if sexo=='m' and idade>=maisvelho:
        nomemaisvelho=nome
        maisvelho=idade
media=idades/4

print("""A média de idade do grupo é de {} anos.
O nome do homem mais velho do grupo é {}.
No grupo há {} mulheres com menos de 20 anos.
""".format(media,nomemaisvelho,mulheresjovens))