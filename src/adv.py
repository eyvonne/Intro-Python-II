from room import Room
from player import Player
from item import Item
from random import choice
from help import print_help
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# make items that are going to be distributed into the rooms
stuff = [
    Item('stick', 'a simple wooden stick, could be used to hit something'),
    Item('rock', 'a rock, what more do you need to know?'),
    Item('boulder', "a large rock, you really shouldn't be able to carry this around"),
    Item('treasure_chest', "A chest full of treatures beyond your wildest imagination"),
    Item('sword', 'a long metal object that looks like it could be used for slicing')
]
# randomly place the items in the rooms
for i in stuff:
    r = choice(list(room))
    room[r].add_item(i)

# Make a new player object that is currently in the 'outside' room.
play = Player('Adventurer', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print(f'hello {play.name}')

while True:
    print()
    print(f"You're in the room: {play.current_room.name}")
    print(play.current_room.desc)
    if len(play.current_room.treasure):
        print('In the room you see: ', end='')
        print(*play.current_room.treasure, sep=', ')
    command = input('What would you like to do? ').split()
    print()

    if command[0].lower() == 'go':
        play.move(command[1])
    elif command[0].lower() == 'grab':
        play.pick_up(command[1])
    elif command[0].lower() == 'drop':
        play.drop(command[1])
    elif command[0].lower() == 'inventory':
        play.show_inventory()
    elif command[0].lower() == 'quit' or command[0].lower() == 'q':
        break
    else:
        print_help(command)
