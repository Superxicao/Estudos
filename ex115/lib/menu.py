pessoas={}

def linha():
    print('-'*40)

def menu():
    linha()
    print(f'{"Menu Principal":^40}')
    linha()
    print("""1 - Ver pessoas cadastradas
2 - Cadastrar Pessoas
3 - Sair do sistema""")
    linha()
    opcoes('Digite sua opção: ')

def pessoas():
    
def cadastrar():
    print('')

def opcoes(msg):
    while True:
        try:
            op=int(input(msg))
        except Exception as e:
            print('\033[41mErro! Digite uma opção válida. Erro: {}\033[m'.format(e))
        else:
            if op==1:
                pessoas()
            elif op==2:
                cadastrar()
            elif op==3:
                break
    print('Volte Sempre!')