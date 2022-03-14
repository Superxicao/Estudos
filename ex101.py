def voto(a):
    from datetime import date
    idade=date.today().year-a
    if idade>60:
       status='OPCIONAL'
    elif idade>17:
        status='OBRIGATÓRIO'
    else:
        status='NÃO VOTA'
    return idade,status
an=int(input('Digite o ano de nascimento: '))
print('Com idade de {}: {}'.format(voto(an)[0],voto(an)[1]))

