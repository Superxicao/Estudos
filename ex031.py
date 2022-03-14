k=float(input('Digite a distância da viagem em km: '))
"""
if k<=200:
    p=k*0.50
else:
    p=k*0.45
"""

p=k*0.50 if k<=200 else k*0.45

print('O valor pra sua viagem fica em {:.2f} reais.'.format(p))