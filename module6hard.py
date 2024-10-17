# Задание "Они все так похожи"
import math

class Figure:
    sides_count = 0

    def __init__(self):
        super().__init__()
        self.__sides = []
        self.__color = []
        self.filled = False

    def get_color(self, *color):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        color_bool = True if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255) else False
        return color_bool

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        sides = list(args)
        for side in sides:
            sides_bool = True if (isinstance(side, int) and len(args) == self.sides_count) else False
        return sides_bool

    def get_sides(self):
        return self.__sides

    def __len__(self):      # периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def set_sides_count(self, sides):          # кол-во сторон
        if self.sides_count != len(sides):
            self.__sides = [sides[0]] * self.sides_count
        return self.__sides


class Circle(Figure):
    sides_count = 1
    __radius = 0

    def __init__(self, color, *sides):   # sides -длина окружности
        super().__init__()
        __sides = sides
        __color = color
        self.set_color(*__color)
        self.set_sides_count(sides)
        self.__radius = sides[0]

    def get_square(self):        # площадь круга
        print(f'\nПлощадь круга: {math.pi * (self.__radius ** 2)}')


class Triangle(Figure):
    sides_count = 3
    a, b, c = 0, 0, 0

    def __init__(self, color, *sides):
        super().__init__()
        __sides = sides
        __color = color
        self.set_color(*__color)
        self.set_sides_count(sides)
        self.a, self.b, self.c = __sides

    def get_square(self):        # площадь треугольника
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(f'\nПлощадь треугольника: {s}')

class Cube(Figure):
    sides_count = 12
    a = 0

    def __init__(self, color, *sides):
        super().__init__()
        __sides = sides
        __color = color
        self.a = int(sides[0])
        self.set_sides_count(sides)
        self.set_color(*__color)

    def get_volume(self):
        # объем куба
        return  self.a ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
