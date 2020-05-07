help_text = f'''
go [direction] - enter n, s, e, or w for direction to move to the room in that direction
grab [item] - enter the name of an item in the current room for item to pick it up
drop [item] - enter the name of an item in your inventory for item to drop it in the current room
inventory - displays items currently in your inventory with descriptions
'''


def print_help(command):
    print(f'{command} is not a valid option. Please Choose from:')
    print(help_text)
