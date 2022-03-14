def fatorial(n,show=False):
    """
    
    """
    res=1
    for x in range(n,0,-1):
        if show:
            if x>1:
                print(x,end=' x ')
            else:
                print(x,end=' = ')
        res*=x
    return res

print(fatorial(5,show=True))