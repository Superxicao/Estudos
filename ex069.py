c=idade=pessoas=homens=mulheres=0
s=continua=''

while True:
    i=int(input('Informe a idade: ')).strip()
    s=str(input('Informe o sexo [F/M]: ')).lower().strip()=[0]
    while s not in 'fm':
        s=str(input('Informe o sexo [F/M]: ')).lower().strip()[0]
    if i>18:
        pessoas+=1
    if s=='m':
        homens+=1
    if s=='f' and i<20:
        mulheres+=1
    while continua not in 'sn':
        continua=str(input('Responda S ou N. Quer continuar? ')).strip().lower()[0]
    if continua=='n':
        break
    c+=1

print(f"""Você cadastrou {c} pessoas.
{pessoas} pessoas tem mais de 18 anos.
{homens} homens foram cadastrados.
{mulheres} mulheres têm menos de 20 anos.""")