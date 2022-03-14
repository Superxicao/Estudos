from exfinal.lib.interface import *
from exfinal.lib.arquivo import *
from time import sleep

arq = 'pessoas.txt'
# a = open(arq, 'rt', encoding='utf-8')

if not arquivoExiste(arq):
    a = open(arq, 'wt+')
    a.close()

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
        lerArquivo(arq)

    elif resposta == 2:
        cabecalho('Opção 2')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrarPessoas(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mErro, {} não é uma opção válida.\033[m'.format(resposta))
    sleep(2)
