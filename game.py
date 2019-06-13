import time
import sys
from room import Room

commands = ['back', 'go', 'help', 'quit']

def location(room):
    room.speak()
    directions = []
    if room.neighbors[0] != '':
        directions.append('north')
    if room.neighbors[1] != '':
        directions.append('east')
    if room.neighbors[2] != '':
        directions.append('south')
    if room.neighbors[3] != '':
        directions.append('west')
    print ('You can go: ', end="", flush=True)
    print(*directions, sep = ", ")  
    directions = []

def run_command(command, room):
    com = command.split()
    if com[0] == 'help':
        print()
        print('You must repair your space suit and investigate what has happened to the space station')
        location(room)
        print('These are the commands you have:')
        print(commands)
    else:
        print('I\'m sorry I don\'t know what you mean')

def print_words(words):
    words = words.split()
    for w in words:
        for c in w:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(' ') # keep in outer loop so only prints spaces between words
		
def play_game():
    playing = True
    print_words('You are standing in an empty hangar')
    print()
    print_words('Your head is throbbing and your space suit has been damaged significantly')
    print()

    # All rooms on map
    hangar = Room('hangar', [])
    briefing_room = Room('briefing room', [])
    cafeteria = Room('cafeteria', [])
    quarters = Room('quarters', [])

    # add rooms models
    # example.add_neighbors(['north neighbor', 'east neighbor', 'south neighbor', 'west neighbor'])
    # no neighbor is denoted as empty strings
    hangar.add_neighbors(['briefing room', 'cafeteria', '', ''])
    briefing_room.add_neighbors(['', 'quarters', 'hangar', ''])
    cafeteria.add_neighbors(['quarters', '', '', 'hangar'])
    quarters.add_neighbors(['', '', 'cafeteria', 'briefing room'])


    the_rooms = [
        hangar,
        briefing_room,
        cafeteria,
        quarters,
    ]

    back_stack = [] # stack to use for going back

    hangar.speak()
    curr_room = hangar
    prev_room = None

    while(playing): 
        user_input = input('> ')	
        user_input = user_input.strip()
        com_split = user_input.split()
        if user_input == None or user_input == '':
            continue
        elif user_input == 'quit' or user_input == 'Quit':
            playing = False
        elif com_split[0] == 'go' and len(com_split) == 1:
            print('Go where? Your choices are north, south, east, and west')
        elif com_split[0] == 'go' and com_split[1] in ['north', 'south', 'east', 'west']:
            if com_split[1] == 'north' and curr_room.neighbors[0] != '':
                # user typed 'go north'
                room_to_find = curr_room.neighbors[0]
                back_stack.append(curr_room)
                for r in the_rooms:
                    if r.name == room_to_find:
                        curr_room = r
                location(curr_room)
            elif com_split[1] == 'east' and curr_room.neighbors[1] != '':
                # user typed 'go east'
                room_to_find = curr_room.neighbors[1]
                back_stack.append(curr_room)
                for r in the_rooms:
                    if r.name == room_to_find:
                        curr_room = r
                location(curr_room)
            elif com_split[1] == 'south' and curr_room.neighbors[2] != '':
                # user typed 'go south'
                room_to_find = curr_room.neighbors[2]
                back_stack.append(curr_room)
                for r in the_rooms:
                    if r.name == room_to_find:
                        curr_room = r
                location(curr_room)
            elif com_split[1] == 'west' and curr_room.neighbors[3] != '':
                # user typed 'go west'
                room_to_find = curr_room.neighbors[3]
                back_stack.append(curr_room)
                for r in the_rooms:
                    if r.name == room_to_find:
                        curr_room = r
                location(curr_room)
            else:
                print('You can\'t go that way!')
        elif com_split[0] == 'back':
            if back_stack == []:
                print('You can\'t go back anymore')
            else:
                curr_room = back_stack.pop()
                location(curr_room)
            # curr_room = prev_room
        else:
            run_command(user_input, curr_room)

def main():
    play_game()

if __name__== "__main__":
    main()

