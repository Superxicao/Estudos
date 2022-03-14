from datetime import date

a=date.today().year
print(a)
jovens=adultos=0

for x in range(7):
    an=int(input('Escreva o nascimento da {}º pessoa:'.format(x+1)))
    if(a-an<18):
        jovens+=1
    else:
        adultos+=1

print("""Você escreveu a data de nascimento de:
{} jovens.
{} adultos.
""".format(jovens,adultos))
