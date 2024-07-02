import json
import pygame


class Cooking:
    def __init__(self):
        with open("../text/cooking/recipes.json", "r") as f:
            self.recipes = json.load(f)
        self.button_default = pygame.image.load("../assets/sprites/UI/Cooking/button_cook_default.png").convert_alpha()
        self.button_hover = pygame.image.load("../assets/sprites/UI/Cooking/button_cook_hover.png").convert_alpha()
        self.button_clicked = pygame.image.load("../assets/sprites/UI/Cooking/button_cook_clicked.png").convert_alpha()
        self.buttons = [self.button_default, self.button_hover, self.button_clicked]
        self.button_index = 0
        self.button_rect = self.button_default.get_rect()
        self.mouse_pressed_on_button = None
        self.cooking_book = pygame.image.load("")
    def cook(self, ingredients, recipe):
        recipe_to_cook = recipe
        needed_ingredients = self.recipes[recipe_to_cook]

        if all(ni in ingredients for ni in needed_ingredients):
            return True, recipe_to_cook
        else:
            return False, None

    def open(self, screen, mouse_pos, mouse_pressed, mouse_released):
        button_clicked = False

        if self.button_rect.collidepoint(mouse_pos):
            if mouse_pressed:
                self.mouse_pressed_on_button = True
                screen.blit(self.buttons[2], self.button_rect)
            elif mouse_released and self.mouse_pressed_on_button:
                button_clicked = True
                screen.blit(self.buttons[1], self.button_rect)
                self.mouse_pressed_on_button = False
            else:
                screen.blit(self.buttons[1], self.button_rect)
        else:
            if mouse_pressed:
                self.mouse_pressed_on_button = False
            screen.blit(self.buttons[0], self.button_rect)

        return button_clicked
