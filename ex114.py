from urllib import request

try:
    request.urlopen('http://www.pudim.com.br')
except:
    print('Inacessível:')
else:
    print('Funcionando!')
finally:
    print('=)')
