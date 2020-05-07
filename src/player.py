# Write a class to hold player information, e.g. what room they are in
# currently.
from typing import List
from item import Item


class Player():
    def __init__(self, name, current_room, inventory: List[Item] = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def pick_up(self, item: str):
        for i in self.current_room.treasure:
            if i.name == item.lower():
                self.current_room.treasure.remove(i)
                self.inventory.append(i)
                i.on_take()
                return
        print(f'No {item} in room to grab')

    def drop(self, item: str):
        for i in self.inventory:
            if i.name == item.lower():
                self.inventory.remove(i)
                self.current_room.treasure.append(i)
                i.on_drop()
                return
        print(f'No {item} in inventory to drop')

    def show_inventory(self):
        print()
        print('Current Inventory: ')
        for i in self.inventory:
            print(f'{i.name}, description: {i.description}')
        print()

    def move(self, playon):
        if playon.lower() == 'n' or playon.lower() == 'north':
            self.current_room = self.current_room.n_to
        elif playon.lower() == 's' or playon.lower() == 'south':
            self.current_room = self.current_room.s_to
        elif playon.lower() == 'e' or playon.lower() == 'east':
            self.current_room = self.current_room.e_to
        elif playon.lower() == 'w' or playon.lower() == 'west':
            self.current_room = self.current_room.w_to
        elif playon.lower() == 'q':
            pass
        else:
            print('Please enter n, s, e, or w with move command')
