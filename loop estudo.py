for n in range(2, 30):
    print('-------\nn =',n)
    for x in range(2, n):
        print('x =',x,end=', ')
        print(n,'%',x,'=',n%x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')




"""
for x in range(2,10):
    print('\nx =',x)
    for y in range(2,x):
        print(x,y, end=', ')
"""