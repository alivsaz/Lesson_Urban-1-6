# Распаковка
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# Примеры вызова функции с параметрами по умолчанию
print(f'1.Функция с параметрами по умолчанию: ')
print_params(33, 'Вася', False)
print_params(b=25)
print_params(c = [1,2,3])
print_params()

print(f'\n2.Распаковка параметров: ')
values_list = (5, 'Телефон', False )
print(values_list)
values_dict = {1:19, 2:'Смартфон', 3:True}
print_params(values_dict)

print(f'\n3.Распаковка + отдельные параметры: ')
values_list_2 = [3.14, 'Alex']
print('values_list_2 = ' + str(values_list_2))
print(f'print_params(*values_list_2, 25) \nВывод на консоль:')
print_params(*values_list_2, 25)
