# Функции в Python.Функция с параметром
def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        if i ==0:
            matrix = [[0 for k in range(m)] for l in range(n)]
        for j in range(m):
            matrix [i][j] = value
    return(matrix)

result1 = 'get_matrix(2, 2, 10)'
result2 = 'get_matrix(3, 5, 42)'
result3 = 'get_matrix(4, 2, 13)'
print(f'Исходный код: '
      f'\nresult1 = {result1}'
      f'\nresult2 = {result2}'
      f'\nresult3 = {result3}')
print(f'\nВывод на консоль:')
print(get_matrix(2,2,10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))