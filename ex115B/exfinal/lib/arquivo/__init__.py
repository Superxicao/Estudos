from exfinal.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<35}{dados[1]:>3}')
    finally:
        a.close()


def cadastrarPessoas(arq, nome='Desconhecido', idade='0'):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mErro na abertura do arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um erro ao escrever os dados.\033[m')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso.')
            a.close()
