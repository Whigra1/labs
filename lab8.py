import random

"""
Доповнити матрицю A(m x n) (m+1)-м рядком та (n+1)-м стовпцем,
в які записати суми елементів відповідних рядків та стовпців вихідної матриці.
В елемент A (m+1, n+1) помістити суму всіх елементів матриці A.
"""

def createMatrix(i, j):
    return [[random.randrange(10) for _ in range(j)] for _ in range(i)]


def main(m, n):
    matrix = createMatrix(m, n)

    for row in matrix:
        row.append(0)

    for ind, row in enumerate(matrix):
        matrix[ind][-1] = sum(row)

    temp = []

    for column in range(len(matrix)):
        res = 0
        for row in matrix:
            res += row[column]
        temp.append(res)
    matrix.append(temp)
    res = 0

    for row in matrix:
        for num in row:
           res += num

    matrix[m][n] = res
    return matrix


if __name__ == '__main__':
    for i in main(5,4):
        print(i)
