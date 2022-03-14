def leiadinheiro(texto):
    while True:
        valor=str(input(texto)).replace(',','.').strip()
        if valor.isalpha() or valor.isalnum() or valor in '':
            print(f'\033[41mERRO! o valor \'{valor}\' não é válido.\033[m')
        else:
            return float(valor)
