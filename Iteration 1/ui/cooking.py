import json
import pygame

class Cooking:
    def __init__(self):
        self.recipes = json.load("recipe.json")
    
    def cook(ingredients, food):
        needed_ingredients = ["Egg", "Toast"]
        
        if ingredients == needed_ingredients:
            text = f"Cooked {food}"
            return True
        else:
            return False