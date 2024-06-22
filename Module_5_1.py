class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        self.new_floor = new_floor
        for i in range(1, self.new_floor + 1):
            if new_floor <= self.number_of_floors:
                print(i)
            else:
                print("Такого этажа не существует")
                break

h_1 = House('ЖК Горский', 18)
h_2 = House('Домик в деревне', 2)
h_3 = House("ЖК Эльюрус", 30)

print(h_1.name, h_1.number_of_floors)
print(h_2.name, h_2.number_of_floors)
print(h_3.name, h_3.number_of_floors)

h_1.go_to(18)
h_2.go_to(4)
h_3.go_to(7)





