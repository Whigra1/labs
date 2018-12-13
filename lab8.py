import random

"""
Доповнити матрицю A(m x n) (m+1)-м рядком та (n+1)-м стовпцем,
в які записати суми елементів відповідних рядків та стовпців вихідної матриці.
В елемент A (m+1, n+1) помістити суму всіх елементів матриці A.
"""

def createMatrix(i, j):
    return [[random.randrange(10) for _ in range(j)] for _ in range(i)]

def column_sum(matrix):
    temp = []
    for column in range(len(matrix)):
        res = 0
        for row in matrix:
            res += row[column]
        temp.append(res)
    return temp


def row_sum(matrix):
    for ind, row in enumerate(matrix):
        matrix[ind][-1] = sum(row)
        

def matrix_sum(matrix):
    res = 0
    for row in matrix:
        for num in row:
           res += num
    return res

def main(m, n):
    matrix = createMatrix(m, n)
    for row in matrix:
        row.append(0)
        
    row_sum(matrix)
    row_tith_sums = column_sum(matrix)
    matrix.append(row_tith_sums)
    matrix[m][n] = matrix_sum(matrix)
    return matrix


if __name__ == '__main__':
    for i in main(5,4):
        print(i)
