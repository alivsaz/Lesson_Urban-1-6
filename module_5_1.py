# Developer - не только разработчик

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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(f"\nИсходные данные:\nh1 = House('{h1.name}', {h1.number_of_floors})")
print(f"h2 = House('{h2.name}', {h2.number_of_floors})")
print(f'h1.go_to(5)\nh2.go_to(10)')
print(f'\nВывод на консоль:')
h1.go_to(5)
h2.go_to(10)
