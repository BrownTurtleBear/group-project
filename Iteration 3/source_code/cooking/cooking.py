import json
import pygame


class Cooking:
    def __init__(self, screen_width, screen_height):
        with open("../text/cooking/recipes.json", "r") as f:
            self.recipes = json.load(f)
        self.button_default = pygame.image.load("../assets/sprites/ui/cooking/button_cook_default.png").convert_alpha()
        self.button_hover = pygame.image.load("../assets/sprites/ui/cooking/button_cook_hover.png").convert_alpha()
        self.button_clicked = pygame.image.load("../assets/sprites/ui/cooking/button_cook_clicked.png").convert_alpha()
        self.buttons = [self.button_default, self.button_hover, self.button_clicked]
        self.button_index = 0
        self.button_rect = self.button_default.get_rect()
        self.mouse_pressed_on_button = None
        original_cooking_book = pygame.image.load("../assets/sprites/ui/cooking/book.png").convert_alpha()
        original_width, original_height = original_cooking_book.get_size()
        self.cooking_book = pygame.transform.scale(original_cooking_book, (original_width * 5.5, original_height * 5.5))
        self.cooking_book_rect = self.cooking_book.get_rect(center=(screen_width / 2, screen_width / 2))

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

    def book(self, screen):
        screen.blit(self.cooking_book, self.cooking_book_rect)
