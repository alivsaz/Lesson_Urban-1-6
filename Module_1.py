# Средний балл
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students) # отсортировать студентов по алфавиту
students_average = {}           # объявляем словарь
i = 0                           # цикл по списку с оценками
for i in range(len(grades)) :
    students_average [students_sort[i]] = sum(grades[i])/len(grades[i])
    i += i
print(students_average)