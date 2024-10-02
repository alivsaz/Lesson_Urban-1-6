# Нужно больше этажей

class House:
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

    # def __str__(self):
    #     string = 'Название: ' + self.name + ', кол-во этажей: ' + str(self.number_of_floors)
    #     return string

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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(f'Пример выполняемого кода:')
print(f"h1 = House('{h1.name}', {h1.number_of_floors})")
print(f"h2 = House('{h2.name}', {h2.number_of_floors})")
print(f'\nВывод на консоль:')
print(f'Название: {h1.name}, кол-во этажей: {h1.number_of_floors}')
print(f'Название: {h2.name}, кол-во этажей: {h2.number_of_floors}')
print(h1 == h2)     # __eq__
h1 = h1 + 10        # __add__
print(f'Название: {h1.name}, кол-во этажей: {h1.number_of_floors}')
print(h1 == h2)     # __eq__
h1 += 10            # __iadd__
print(f'Название: {h1.name}, кол-во этажей: {h1.number_of_floors}')
h2 = 10 + h2        # __radd_
print(f'Название: {h2.name}, кол-во этажей: {h2.number_of_floors}')
print(h1 > h2)      # __gt__
print(h1 >= h2)     # __ge__
print(h1 < h2)      # __lt__
print(h1 <= h2)     # __le__
print(h1 != h2)     # __ne__