# Слишком древний шифр
def pair_of_numbers(pair):
    password = ''
    for i in range(1,19):
        for j in range(1,pair):
            if pair%(i+j) == 0 and i<j:
                password = password + str(i) + str(j)
    return (password)

code = int(input('Введите код (число от 3 до 20): '))
result = pair_of_numbers(code)
print(f'\nРезультат - комбинация "КОД - ПАРОЛЬ": \n{code} - {result} ')
