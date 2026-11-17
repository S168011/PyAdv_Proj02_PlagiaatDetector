import json

class BuildingVisitor:
    def do_something_for_industrial(self, i):
        print(json.dumps(i.__dict__))
    
    def do_something_for_residential(self, r):
        print(json.dumps(r.__dict__))


class Industrial:
    def __init__(self, co2: int) -> None:
        self.co2 = co2

    def accept(self, visitor):
        visitor.do_something_for_industrial(self)

class Residential:
    def __init__(self, bedrooms: int, surface: int) -> None:
        self.bedrooms = bedrooms
        self.surface = surface

    def accept(self, visitor):
        visitor.do_something_for_residential(self)

# veronderstel dat er een lijst gebouwen is

buildings = [Industrial(500), Residential(2, 50), Residential(3, 150)]

building_visitor = BuildingVisitor()

for building in buildings:
    building.accept(building_visitor)