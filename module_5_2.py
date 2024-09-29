# Магические здания

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

    def __str__(self):
        string = 'Название: ' + self.name + ', кол-во этажей: ' + str(self.number_of_floors)
        return string

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(f'Пример выполняемого кода:')
print(f"h1 = House('{h1.name}', {h1.number_of_floors})")
print(f"h2 = House('{h2.name}', {h2.number_of_floors})")
print(f'\nВывод на консоль:')
print(h1.__str__())
print(h2.__str__())
print(h1.__len__())
print(h2.__len__())