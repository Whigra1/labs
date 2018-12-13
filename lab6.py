"Дано натуральне число n. Отримати всі прості дільники цього числа"
def func(n):
    res = []
    for i in range(1,n):
        if n % i == 0:
            if simple(i):
                res.append(i)
    return res


def simple(n):
	for i in range(2,n):
		if n % i == 0:
			return False
	return True


if __name__ == '__main__':
    for i in range(101):
        print(i,func(i))
    
