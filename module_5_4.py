# метод __new__

class House:
    __first = 0
    def __new__(cls, *args, **kwargs):
        if cls.__first == 0:
            cls.houses_history = []
            cls.__first = 1
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if (new_floor < 0) or (new_floor > self.number_of_floors):
            print('"Такого этажа не существует"')
        else:
            for i in range(new_floor):
                print(i+1)

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'"{other}" нельзя сравнить с "{self.number_of_floors}", '
                  f'т.к. оно не является целым числом')
            return
        else:
            return (self.number_of_floors == other.number_of_floors)

    def __lt__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'"{other}" нельзя сравнить с "{self.number_of_floors}", '
                  f'т.к. оно не является целым числом')
            return
        else:
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'"{other}" нельзя сравнить с "{self.number_of_floors}", '
                  f'т.к. оно не является целым числом')
            return
        else:
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'"{other}" нельзя сравнить с "{self.number_of_floors}", '
                  f'т.к. оно не является целым числом')
            return
        else:
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'"{other}" нельзя сравнить с "{self.number_of_floors}", '
                  f'т.к. оно не является целым числом')
            return
        else:
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'"{other}" нельзя сравнить с "{self.number_of_floors}", '
                  f'т.к. оно не является целым числом')
            return
        else:
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            print(f'"{value}" не является целым числом')
        return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
        if not isinstance(value, int):
            print(f'"{value}" не является целым числом')
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        if not isinstance(value, int):
            print(f'"{value}" не является целым числом')
        return House(self.name, self.number_of_floors + value)


print(f'\nВывод на консоль:')
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)
