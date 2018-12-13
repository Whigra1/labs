"Дано натуральне число n. Отримати всі прості дільники цього числа"
def func(n):
    res = []
    for i in range(1,n):
        if n % i == 0:
            if simple(i):
                res.append(i)
    return res


def simple(i):
    if i < 10:
        if i == 3 or i == 2 or i == 5 or i == 7:
            return True
    else:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            return True
    return False


if __name__ == '__main__':
    for i in range(101):
        print(i,func(i))
    
