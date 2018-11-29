"""
1.Задані цілочисельні масиви А(n) і В(n). Побудувати масив С(n),
кожен елемент якого є добутком максимального елемента даних масивів
і найбільшого спільного дільника елементів аі і bі.
Для знаходження найбільшого спільного дільника
чисел використати алгоритм Евкліда.
"""

def evclid(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a+b


def main(a,b):
    res = []
    for i in range(len(a)):
        res.append(max(a)*max(b)*evclid(a[i],b[i]))
    return res


if __name__ == '__main__':

    print(main([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
