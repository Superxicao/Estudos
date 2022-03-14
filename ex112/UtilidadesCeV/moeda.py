def aumentar(n,taxa,formato=False):
    aumento=n+(n*taxa/100)
    return aumento if formato is False else moeda(aumento)

def diminuir(n,taxa,formato=False):
    diminui=n-(n*taxa/100)
    return diminui if formato is False else moeda(diminui)

def dobro(n,formato=False):
    dobro=n*2
    return dobro if formato is False else moeda(dobro)

def metade(n,formato=False):
    metade=n/2
    return metade if formato is False else moeda(metade)

def moeda(n=0, moeda='R$'):
        return f'{moeda}{n:.2f}'.replace('.',',')

def resumo(n,a,r):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f"""{'Preço Analisado:':<20}{moeda(n):<10}
{'Dobro do Preço:':<20}{dobro(n,True):<10}
{'Metade do preço':<20}{metade(n,True):<10}
{a}% {'de Aumento:':<16}{aumentar(n,a,True):<10}
{r}% {'de Redução:':<16}{diminuir(n,r,True):<10}""")
    print('-'*30)