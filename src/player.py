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
        for i in self.current_room.items:
            if i.name == item.lower():
                self.current_room.items.remove(i)
                self.inventory.append(i)

    def drop(self, item: str):
        for i in self.inventory:
            if i.name == item.lower():
                self.inventory.remove(i)
                self.current_room.items.append(i)
