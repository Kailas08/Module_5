class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

build_1 = Building(20, 'Кирпичное')
build_2 = Building(20, 'Кирпичное')

if build_1 == build_2:
    print('Оба здания одинаковые')
else:
    print('Здания разные')
