times=('Bahia','Ceará','Fortaleza','Flamengo','São Paulo','Fluminense',
       'Athletico-PR','Juventude','Corinthians','Atlético-GO','América-MG',
       'Cuiabá','Esporte','Chapecoense','Red Bull Bragantino','Internacional',
       'Sport','Grêmio','Atlético-MG','Palmeiras','Santos')

for t in times:
    print(t)

for t in range(0,len(times)):
    print(times[t],end=' ')

for pos,t in enumerate(times):
    print(pos,t)

print(f'Os 5 primeiros times são: {times[0:5]}')
print(f'Os últimos 4 times são: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print('Chapecoence está na {}° posição.'.format(times.index('Chapecoense')))

d=0
for c in times:
    if c=='Chapecoense':
        print(f'Chapecoense está na {d}° posição')
        break
    d+=1

for c in range(0,len(times)):
    if times[c]=='Chapecoense':
        print(f'Chapecoense está na {c}° posição.')
i=0
while True:
    if times[i]=='Chapecoense':
        print('Chapecoense está na {}° posição.'.format(i))
        break
    i+=1