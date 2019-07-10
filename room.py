from people import Person

class Room:

    def __init__(self, name, neighbors, items, habitant):
        self.name = name
        self.neighbors = []
        self.items = []
        self.habitant = None

    def speak(self):
        print('You are in the ' + self.name)
	
    def add_neighbors(self, rooms):
        for n in rooms:
            self.neighbors.append(n)

    def add_items(self, objects):
        for i in objects:
            self.items.append(i)

    def remove_item(self, obj):
        self.items.remove(obj)

    def add_item(self, obj):
        self.items.append(obj)

    def make_person(self, person_info):
        name = person_info[0]
        saying = person_info[1]
        human = Person(name, saying)
        self.habitant = human

