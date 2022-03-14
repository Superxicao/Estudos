sexo=''
cont=homens=mulheres=0

while sexo!='s':
    sexo=str(input('Digite o sexo("s" para sair) [M/F]: ').lower()[0])
    if sexo not in 'mfs':
       sexo=str(input('Digite um sexo válido: '))
    if sexo=='f':
        mulheres+=1
    elif sexo=='m':
        homens+=1
    cont+=1
print('Você respondeu {} vezes.\n{} são homens e {} são mulheres.'.format(cont-1,homens,mulheres))
    
