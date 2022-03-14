from datetime import date

s=str(input('Digite seu sexo, M ou F?: ').lower())

if s=='m':
    print('\033[45mVocê pode se alistar. Vamos verificar sua possibilidade de alistamento.\033[m')
    an=int(input('\033[33mDigite o ano de nascimento: \033[m'))
    a=date.today().year
    idade=a-an
    if idade<18:
        print('\033[7;1;40mPara quem nasceu em {} e tem {} anos de idade o alistamento será daqui a {} anos no ano de {}.\033[m'.format(an,idade,18-idade,an+18))
    elif idade==18:
        print('\033[1;7;4;40mPara quem nasceu em {} e tem {} anos, o alistamento é esse ano!\n Estamos em {}.\033[m'.format(an,idade,a))
    else:
        print('\033[1;7mPara quem nasceu em {} e tem {} anos de idade, o alistamento já passou há {} anos, pois deveria ter sido em {}.\033[m'.format(an,idade,idade-18,an+18))

elif s=='f':
    print('\033[45mVocê é mulher, seu alistamento não é obrigatório.\033[m')


"""
from datetime import date

s=str(input('Digite seu sexo, M ou F?: ').lower())

if s=='m':
    print('\033[45mVocê pode se alistar. Vamos verificar sua possibilidade de alistamento.\033[m')
    an=int(input('\033[33mDigite o ano de nascimento: \033[m'))
    a=date.today().year
    idade=a-an
if idade<18:
    print('\033[7;1;40mPara quem nasceu em {} e tem {} anos de idade o alistamento será daqui a {} anos no ano de {}.\033[m'.format(an,idade,18-idade,an+18))
elif idade==18:
    print('\033[1;7;4;40m1Para quem nasceu em {} e tem {} anos, o alistamento é esse ano!\n Estamos em {}.\033[m'.format(an,idade,a))
elif idade>18:
    print('\033[1;7mPara quem nasceu em {} e tem {} anos de idade, o alistamento já passou há {} anos, pois deveria ter sido em {}.\033[m'.format(an,idade,idade-18,an+18))
elif s=='f':
    print('\033[45mVocê é mulher, seu alistamento não é obrigatório.\033[m')

    """
