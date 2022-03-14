casa=float(input('Digite o valor da casa: '))
salario=float(input('Digite o valor do seu salario: '))
anos=float(input('Digite em quantos anos pretende pagar: '))

prestacao=casa/(anos*12)

print("""\033[31mO valor da casa é R${:.2f} reais;\033[m
\033[36mSeu salário é de R${:.2f} reais;\033[m
\033[33mVocê solicitou pagar em {:.2f} anos;\033[m
\033[1;4;35mAs prestações ficariam em R${:.2f} reais por mês;\033[m
""".format(casa,salario,anos,prestacao),end='')

if prestacao>salario*30/100:
    print('\033[32mInfelizmente não podemos te conceder o empréstimo.\033[m\033[1;7;30;43m:/\033[m')
else:
    print('{}Empréstimo concedido!{}'.format('\033[7;40m','\033[m'))