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
    print(func(1))
    print(func(2))
    print(func(3))
    print(func(4))
    print(func(5))
