# Подробнее о функциях

def calculate_structure_sum(*param):
    global my_sum
    if isinstance(*param, dict):
        my_list = list(dict(*param).items())
        i,j = 1,1
        for i in range(len(my_list)):
            for j in range(len(my_list[i])):
                calculate_structure_sum(my_list[i][j])
    elif (isinstance(*param, list) or isinstance(*param, tuple)
          or isinstance(*param, set)):
        my_list = list(*param)
        i = 1
        for i in range(len(my_list)):
            calculate_structure_sum(my_list[i])
        else:
            return (my_sum)
    elif isinstance(*param, str):
        my_sum += len(*param)
    else:
        my_sum += param[0]

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

my_sum = 0
print(f'Входные данные:\n{data_structure}')
result = calculate_structure_sum(data_structure)
print(f'\nВыходные данные:\n{result}')