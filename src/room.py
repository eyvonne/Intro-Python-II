# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
from typing import List


class Room():
    def __init__(self, name: str, description: str, treasure=[]):
        self.name = name
        self.desc = description
        self.treasure = treasure

    def __getattr__(self, attr):
        if attr[-3:] == '_to':
            print(f"There isn't a room to the {attr.strip('_to')}")
            return self
        else:
            raise AttributeError(f'{self.name} has no attribute {attr}')

    def add_item(self, item: Item):
        self.treasure.append(item)
