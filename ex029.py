v=int(input('Digite a velocidade: '))

if v>80:
    m=(v-80)*7
    print('Você foi multado! Sua velocidade foi de {}km/h, sua multa é de R$ {},00 Reais.'.format(v,m))
else:
    print('Velocidade de {}km/h ok.'.format(v))