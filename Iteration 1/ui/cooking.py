import json

class Cooking:
    def __init__(self, filename):
        self.recipes = self.load_recipes(filename)

    def load_recipes(self, filename):
        with open(filename, 'r') as file:
            recipes = json.load(file)
        return recipes

    def check_recipes(self, items):
        matching_recipes = []
        items_set = set(items)

        for recipe in self.recipes:
            ingredients_set = set(recipe["ingredients"])
            if ingredients_set.issubset(items_set):
                matching_recipes.append(recipe["recipe"])

        return matching_recipes