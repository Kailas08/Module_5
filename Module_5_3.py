class Building:
    total = 0

    def __init__(self):
        Building.total += 1

for i in range(1, 41):
    Building()
    print('Объект № ', i)
