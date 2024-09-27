# Пространство имен

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

# Вызов inner_function вне функции test_function
# def test_function():
#     def inner_function():
#         print('Я в области видимости функции test_function')
#
# inner_function()