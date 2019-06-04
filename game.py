import time
import sys
from room import Room

commands = ['go', 'back', 'quit', 'help']

def run_command(command):
	com = command.split()
	if com[0] == 'help':
		print('You must repair your space suit and investigate what has happened to the space station')
		print('These are the commands you have:')
		print(commands)
	elif com[0] == 'go' and len(com) == 1:
		print('Go where? Your choices are north, south, east, and west')
	elif com[0] == 'go' and com[1] in ['north', 'south', 'east', 'west']:
		print('hi')
	elif com[0] == 'back':
		print('back')
		# TODO
	else:
		print('I\'m sorry I don\'t know what you mean')

def print_words(words):
	words = words.split()
	for w in words:
		for c in w:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.1)
		sys.stdout.write(' ')
		
def play_game():
	playing = True
	print_words('You are standing in an empty hanger')
	print()
	print_words('Your head is throbbing and your space suit has been damaged significantly')
	print()

	start_room = Room('hangar', [])
	start_room.add_neighbors(['briefing room', 'cafeteria', '', ''])

	briefing_room = Room('briefing room', [])
	briefing_room.add_neighbors(['', 'hangar', '', ''])

	start_room.speak()

	curr_room = start_room

	while(playing): 
		user_input = input('> ')	
		if user_input == 'quit' or user_input == 'Quit':
			playing = False
		elif user_input == None or user_input == '': 
			continue
		else:
			run_command(user_input)

def main():
	play_game()

if __name__== "__main__":
	main()
