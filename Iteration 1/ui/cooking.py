import json
import pygame


class Cooking:
    def __init__(self):
        with open(r"Iteration 1\ui\recipes.json", "r") as f:
            self.recipes = json.load(f)
            
    
    def cook(self, ingredients, food):
        
        needed_ingredients = self.recipes[food]
        
        if all(ni in ingredients for ni in needed_ingredients):
            return True, food
        else:
            return False, None