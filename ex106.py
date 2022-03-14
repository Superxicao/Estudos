from time import sleep
c=('\033[m',    # 0 - Sem cor
   '\033[41m',  # 1 - Vermelho
   '\033[42m',  # 2 - Verde
   '\033[43m',  # 3 - Amarelo
   '\033[44m',  # 4 - Azul
   '\033[45m',  # 5 - Roxo
   '\033[7;40m'   # 6 - Branco
)

def ajuda(com):
    print(f'Acessando o comando \'{com}\'...',4)
    titulo('PYHELP')
    print(c[6],end='')
    help(com)
    print(c[0],end='')
    sleep(2)

def titulo(msg,cor=0):
    tam=len(msg)+4
    print(c[cor],end='')
    print('='*tam)
    print(f'  {msg:^}')
    print('='*tam)
    print(c[0],end='')
    sleep(1)

while True:
    titulo('SISTEMA DE AJUDA PYHELP',2)
    comando=str(input('Função ou Biblioteca> ')).lower().strip()
    if comando in 'fimsair':
        titulo('FIM')
        break
    ajuda(comando)

titulo('ATÉ LOGO',1)