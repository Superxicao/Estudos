#3
n=list(int(input('Digite o número: ')) for x in range(4))
print(f'O maior elemento é {max(n)} na posição',', '.join(str(x) for x in n if x==max(n)),end='')
print(f' e o menor é {min(n)} na posição',', '.join(str(x) for x in n if x==min(n)))
print(n)












""" 2
n=list(int(input('Digite um número: ')) for x in range(4))
print(f'O maior número é {max(n)} na posição',', '.join(str(x) for x in range(4) if x==max(n)))
print(f'O menor número é {min(n)} na posição',', '.join(str(x) for x in range(4) if x==min(n)))












n=list(int(input('Digite o valor: ')) for c in range(4))
print(f'O maior número é {max(n)} na posição',', '.join(str(c) for c in range(4) if n[c]==max(n)),end='')
print(f' e o menor é {min(n)} na posição',', '.join(str(c) for c in range(4) if n[c]==min(n)))


Emanoel Delfino
há 1 ano (editado)
Fiz em 4 linhas de código:

n = [int(input(f'\nDigite um valor para a posição {pos}: ')) for pos in range(5)]
print(f'\nVocê digitou os valores {n}.')
print(f'\nMaior nº digitado foi {max(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == max(n))}.')
print(f'Menor nº digitado foi {min(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == min(n))}.')

Para quem tiver maior interesse meu repositório no GitHub com os exercícios resolvidos: github.com/emanoeldelfino/pycev"""