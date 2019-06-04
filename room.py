class Room:

	def __init__(self, name, neighbors):
		self.name = name
		self.neighbors = []

	def speak(self):
		print('You are in the ' + self.name)
	
	def add_neighbors(self, rooms):
		for n in rooms:
			self.neighbors.append(n)

