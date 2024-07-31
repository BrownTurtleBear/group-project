import pygame


class Inventory:
    def __init__(self):
        self.items = {}
        self.recipes = []
        self.dishes = {}

    def add_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name]['quantity'] += quantity
        else:
            self.items[item.name] = {'item': item, 'quantity': quantity}
        print(f"added item {item} (x{quantity})")

    def add_recipe(self, recipe):
        if recipe in self.recipes:
            return False
        else:
            self.recipes.append(recipe)

    def add_dish(self, dish, quantity):
        if dish.name in self.items:
            self.dishes[dish.name]['quantity'] += quantity
        else:
            self.dishes[dish.name] = {'item': dish, 'quantity': quantity}
        print(f"added item {dish} (x{quantity})")

    def remove_item(self, item, quantity):
        if item.name in self.items:
            if self.items[item.name]['quantity'] > quantity:
                self.items[item.name]['quantity'] -= quantity
            elif self.items[item.name]['quantity'] == quantity:
                del self.items[item.name]

    def remove_dish(self, dish, quantity):
        if dish.name in self.dishes:
            if self.dishes[dish.name]['quantity'] > quantity:
                self.dishes[dish.name]['quantity'] -= quantity
            elif self.dishes[dish.name]['quantity'] == quantity:
                del self.dishes[dish.name]

    def move_item(self, item_name, new_position):
        if item_name in self.items:
            self.items[item_name]['item'].inventory_pos = new_position
