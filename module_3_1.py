# Счётчик вызовов
def count_calls():
    global calls
    calls += 1

def string_info(string):
    info = list()
    info.extend([len(string), string.upper(), string.lower()])
    my_tuple = tuple(info)
    return (my_tuple)

def is_contains(list_to_search, string):
    list_to_search_lower = list_to_search.lower()
    string_lower = [i.lower() for i in string]
    return(list_to_search_lower in string_lower)

calls = 0
print(string_info('Владивосток'))
count_calls()
print(string_info('Хабаровск'))
count_calls()
print(is_contains('Владивосток', ['Тула', 'ВладивостоК', 'Минск']))
count_calls()
print(is_contains('Хабаровск', ['Тюмень', 'Астрахань']))
count_calls()
print(calls)