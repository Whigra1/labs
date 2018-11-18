

def f(x,y):
    return x*x - y*y


def g(x,y,z):
    down = 4*z*y
    if down == 0:
        print('Zero Division')
        raise ValueError
    else:
        res = (x + y) / down
    return res


def main(a, b, c, d):
    first_part_up = f(a, c) + f(c, d)
    first_part_down = math.sqrt(g(a, b, c))  
    second_part_up = c - g(a, b, c) + 1
    second_part_down = f(b, c) - f(a, b)    
    third_part_up = math.sqrt(g(a,b,c))
    third_part_down = f(b, c) - f(a, c)    
    return (first_part_up/first_part_down) + (second_part_up/second_part_down) * (1 + third_part_up/third_part_down)


if __name__ == '__main__':
    print(main(15,1,6,1))

    
