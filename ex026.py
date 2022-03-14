f=str(input('Digite uma frase: ')).strip()
f1=f.lower()
f2=f.lower().count('a')
f3=f1.count('a')
f4=f1.find('a')
f5=f1.rfind('a')

print("""
A letra A aparece {} vezes.
Sua primeira posição é: {}.
Sua última posição é: {}.
""".format(f3,f4,f5))

f=str(input('Digite uma frase: ')).upper().strip()

print('A letra "a" aparece na palavra {} vezes.\nA primeira vez é na posição {}, e a última vez é na posição {}.'.format(f.count('A'),f.find('A'),f.rfind('A')))