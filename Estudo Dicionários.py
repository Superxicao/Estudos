posses={'homens':
{'Paulo':['carro',['fusca','palio'],
'casa',['iguaba','recreio','realengo'],
'mulher',['esposa','amante','outras']],

'Rogégio':{'carro':['corola','s10'],
'casa':['barra','leblon'],
'mulher':['favelada','casada']}}}

print(posses)

for x in posses[0]:
    for y,z in posses[0]['homens'].items():
        print(y,z)