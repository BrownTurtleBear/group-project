import pygame


class Inventory:
    def __init__(self):
        self.items = {}
        self.recipes = []

    def add_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name]['quantity'] += quantity
        else:
            self.items[item.name] = {'item': item, 'quantity': quantity}

    def add_recipe(self, recipe):
        if recipe in self.recipes:
            return False
        else:
            self.recipes.append(recipe)

    def move_item(self, item_name, new_position):
        if item_name in self.items:
            self.items[item_name]['item'].inventory_pos = new_position
