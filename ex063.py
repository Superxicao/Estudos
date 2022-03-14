cont=a=0
max=b=1

while max!=0:
    min=0
    max=int(input('Quantos termos você quer? '))
    while min<max:
        print(a,end=' ')
        a=a+b
        b=a-b
        cont+=1
        min+=1
    print('')

print(f'Você escolheu {cont} termos.')

"""
se tu tiver com Guanabara e sentirvontade de fazer o que eu vou te pedir, mostra pra ele esse código q eu criei da sequencia fibonacci, sei que ele vai amar kk
a=0
b=1
while...
print(a)
a=a+b
b=a-b

se nao sem prob tb, é q descobri esse codigo e fiquei empolgado kk

"""