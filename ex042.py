a=int(input('Digite a medida do primeiro lado: '))
b=int(input('Digite a medida do segundo lado: '))
c=int(input('Digite a medida do terceiro lado: '))
d=('As medidas são {}, {} e {}. Triângulo'.format(a,b,c))


if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print(d,'Equilátero.')
    elif a==b or b==c or a==c:
        print(d,'Isósceles.')
    elif a!=b!=c!=a:
        print(d,'Escaleno.')
else:
    print('Não formam um triângulo.') 
