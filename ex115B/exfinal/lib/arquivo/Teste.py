a = int(input("Digite um número: "))
b = int(input("digite outro número: "))

if a>b:
    print("o número {} é maior que {}.".format(a,b))
else:
    print("Já que o número não é maior que b, então te mostro o número {}.".format(b))

for x in range(a):
    print(x)