# Неизменяемые и изменяемые объекты. Кортежи и списки
immutable_var = True, 'Юрий', 'Андрей', 44
print('Неизменяемый кортеж: '+str(immutable_var))
# immutable_var [1] = 'Жанна'    - ошибка (кортеж относиться к неизменяемым объектам)
mutable_list = ([True, 'Юрий', 'Андрей', 44])
mutable_list [2] = 'Жанна'
print('Изменяемый список: '+str(mutable_list))