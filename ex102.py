def fatorial(n,show=False):
    """
    Função Fatorial:
    n: Número que quer ser fatorado.
    show: Define se quer que exiba o processo do cálculo.
    res: Resultado que vai se acumulando da fatoração.
    return: Retorna o resoltado final do cálculo.
    """
    res=n
    if show:
        print(n,end=' ')
    for x in range(n,0,-1):
        y=x-1
        if x==1:
            print('=',end=' ')
            return res
        res*=y
        if show:
            print(f'x {x-1}',end=' ')    
print(fatorial(5))
help(fatorial)
