# Операторы if, elif, else.
print(f'Введите три целых числа')
first = input('Первое: ')
second = input('Второе: ')
third = input('Третье: ')
print(f'\nВвод в консоль: \n{first} \n{second} \n{third}')
if first == second and first == third:
    print(f'\nВывод в консоль: \n3')
elif first == second or first == third or second == third:
    print(f'\nВывод в консоль: \n2')
else:
    print(f'\nВывод в консоль: \n0')