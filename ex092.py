from datetime import datetime
a=datetime.now().year

#from datetime import date
#a=date.today().year

pessoas=dict()
pessoas['Nome']=str(input('Digite o nome: ')).strip()
pessoas['Ano de Nascimento']=int(input('Digite o Ano de Nascimento: '))
pessoas['Idade']=a-pessoas['Ano de Nascimento']
pessoas['CTPS']=int(input('Digite o CTPS (0 não tem): '))
if pessoas['CTPS']!=0:
    pessoas['Ano de Contratação']=int(input('Digite o Ano de Contratação: '))
    pessoas['Salário']=float(input('Digite o salário: '))
    pessoas['Idade da Aposentadoria']=(pessoas['Ano de Contratação']+35)-pessoas['Ano de Nascimento']

for k,v in pessoas.items():
    print('{} tem o valor {}.'.format(k,v))