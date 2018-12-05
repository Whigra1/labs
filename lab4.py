start = 1
n = 1

def func_rec(num,x,n):
    if x < 0 or x > 4:
        raise Exception('x не входит в одз')
    
    res = num * (-1 * pow(x, 2) /
                (2 * n * (2 * n - 1)))
    
    if abs(res - num) < 0.001:
        return num
    else:
        return num + func_rec(res,x,n+1)


def func(x):
    if x < 0 or x > 4:
        raise Exception('x не входит в одз')
    total = 1
    start = 1
    delta = 0
    n = 1
    while abs(start - delta) > 0.001:
        delta = start
        start = start * (-1 * pow(x, 2) /
                         (2 * n * (2 * n - 1)))
        total += start
        n += 1
        
    return total


if __name__ == '__main__':
    print(func_rec(start, 2, n))
