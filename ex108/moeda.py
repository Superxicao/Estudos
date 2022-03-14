def aumentar(n,taxa):
    aumento=n+(n*taxa/100)
    return aumento

def diminuir(n,taxa):
    diminui=n-(n*taxa/100)
    return diminui

def dobro(n):
    dobro=n*2
    return dobro

def metade(n):
    metade=n/2
    return metade

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')