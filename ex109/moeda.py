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