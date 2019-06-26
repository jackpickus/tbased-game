class Room:

    def __init__(self, name, neighbors, items):
        self.name = name
        self.neighbors = []
        self.items = []

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
