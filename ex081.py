c=0
n=[]
while True:
    n.append(int(input('Digite um número: ')))
    p='k'
    c+=1
    while p not in 'sn':
        p=str(input('Quer cotinuar [S/N]? ')).strip().lower()
    if p=='n':
        break

n.sort(reverse=True)
print(f"""A lista ficou: {n}
Ao todo foram digitados {c} números, {len(n)} vezes.
A lista de valores ordenada de forma decrescente é: {n[::-1]}""",
f"""\nO valor 5 foi digitado {n.count(5)} vezes.""" if n.count(5)>0 else
"""\nO valor 5 não foi digitado.""")
