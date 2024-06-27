import json
import pygame


class Cooking:
    def __init__(self):
        with open(r"Iteration 1\ui\recipes.json", "r") as f:
            self.recipes = json.load(f)
        self.button_default = pygame.image.load("Iteration 1/assets/ui/cooking/button_cook_default.png")
        self.button_hover = pygame.image.load("Iteration 1/assets/ui/cooking/button_cook_hover.png")
        self.button_clicked = pygame.image.load("Iteration 1/assets/ui/cooking/button_cook_clicked.png")
        self.buttons = [self.button_default, self.button_hover, self.button_clicked]
        self.button_index = 0
        self.button_rect = self.button_default.get_rect()

    def cook(self, ingredients, food):

        needed_ingredients = self.recipes[food]

        if all(ni in ingredients for ni in needed_ingredients):
            return True, food
        else:
            return False, None

    def open(self, screen, mouse_pos, mouse_pressed):
        if self.button_rect.collidepoint(mouse_pos):
            if mouse_pressed == 1:
                button_index = 2
            else:
                button_index = 1
        else:
            button_index = 0

        screen.blit(self.buttons[button_index])
