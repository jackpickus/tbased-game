from room import Room
from PrintOut import print_words
from Map import *

COMMANDS = ['back', 'backpack', 'drop', 'go', 'help', 'map', 'pickup', 'talk', 'quit', 'search']
backpack = []
secret_room_open = False

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
    print('You can go: ', end="", flush=True)
    print(*directions, sep=", ")
    directions = []

def run_command(command, room):
    global secret_room_open
    com = command.split()
    if com[0] == 'help':
        print()
        print('You must repair your space suit and investigate what has happened to the space station')
        location(room)
        print('These are the commands you have:')
        print(COMMANDS)
    elif com[0] == 'map':
        if secret_room_open:
            show_secret_map()
        else:
            show_map()
    elif com[0] == 'pickup' and len(com) == 2:
        if com[1] in room.items:
            backpack.append(com[1])
            room.remove_item(com[1])
            print_words('You just picked up ' + com[1])
            if com[1] == 'key':
                COMMANDS.append(com[1])
        else:
            print_words('Does not compute. Try using \'pickup\' another way')
    elif com[0] == 'drop' and len(com) == 2:
        if com[1] in backpack:
            backpack.remove(com[1])
            room.add_item(com[1])
            print_words('You just dropped ' + com[1])
        else:
            print_words('Does not compute. Try using \'drop\' another way')
    elif com[0] == 'backpack':
        print_words('You have these items in your backpack: ' + str(backpack))
    elif com[0] == 'search':
        if room.items == []:
            print_words('There are no items here')
        else:
            print_words('As you look around the room you see these items')
            print(room.items)
    elif com[0] == 'key' and 'key' in backpack and room.name == 'briefing room':
        COMMANDS.remove('key')
        backpack.remove('key')
        print_words('Using the key you found, the secret room has been opened')
        secret_room_open = True
    elif com[0] == 'talk':
        if room.habitant is not None:
            room.habitant.speak()
        else:
            print_words('There is no one here to talk to')
    else:
        print('I\'m sorry I don\'t know what you mean')

def play_game():
    playing = True
    print_words('You are standing in an empty hangar')
    print_words('Your head is throbbing and your space suit has been damaged significantly')

    # All rooms on map
    # room structure: Room('name', [neighbors], [items], [people in room])
    hangar = Room('hangar', [], [], [])
    briefing_room = Room('briefing room', [], [], [])
    cafeteria = Room('cafeteria', [], [], [])
    quarters = Room('quarters', [], [], [])
    secret = Room('secret room', [], [], [])

    # add rooms models
    # example.add_neighbors(['north neighbor', 'east neighbor', 'south neighbor', 'west neighbor'])
    # no neighbor is denoted as empty strings
    hangar.add_neighbors(['briefing room', 'cafeteria', '', ''])
    briefing_room.add_neighbors(['', 'quarters', 'hangar', 'secret room'])
    cafeteria.add_neighbors(['quarters', '', '', 'hangar'])
    quarters.add_neighbors(['', '', 'cafeteria', 'briefing room'])
    secret.add_neighbors(['', 'briefing room', '', ''])

    cafeteria.add_items(['key'])
    quarters.add_items(['tape'])

    the_rooms = [
        hangar,
        briefing_room,
        cafeteria,
        quarters,
        secret
    ]

    back_stack = [] # stack to use for going back

    hangar.speak()
    curr_room = hangar

    survivor_info = ['Survivor', 'You must find the key and unlock the room']
    briefing_room.make_person(survivor_info)

    global secret_room_open # boolean for unlocking room

    while playing:

        user_input = input('> ')
        user_input = user_input.strip()
        com_split = user_input.split()
        if user_input is None or user_input == '':
            continue
        elif user_input in ('quit', 'q'):
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
                if room_to_find == 'secret room' and not secret_room_open:
                    print_words('This door is locked.')
                else:
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
        else:
            run_command(user_input, curr_room)

def main():
    play_game()

if __name__ == "__main__":
    main()
    