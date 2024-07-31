from items.dishes import Dish


class Recipe:
    def __init__(self, name, ingredients, description=None):
        self.name = name
        self.ingredients = ingredients
        self.description = description
        self.dish = Dish(name, (8, 9), description)
