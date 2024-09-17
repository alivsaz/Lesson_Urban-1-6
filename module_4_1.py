# Модули и пакеты

from fake_math import divide as div_fake
from true_math import divide as div_true

result1 = div_fake(69, 3)
result2 = div_fake(3, 0)
result3 = div_true(49, 7)
result4 = div_true(15, 0)

print(f'Вывод на консоль:\n{result1}\n{result2}\n{result3}\n{result4}')