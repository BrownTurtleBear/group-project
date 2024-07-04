import pygame
from controls.mouse_tracker import MouseTracker

mouse_tracker = MouseTracker()


def cook(inventory, recipe):
    needed_ingredients = inventory.recipes[recipe]
    if all(ni in inventory for ni in needed_ingredients):
        return True
    else:
        return False


class Cooking:
    def __init__(self, screen, screen_width, inventory):
        self.screen = screen
        self.inventory = inventory
        self.screen_width = screen_width
        # Book
        original_cooking_book = pygame.image.load("../assets/sprites/ui/cooking/book.png").convert_alpha()
        original_width, original_height = original_cooking_book.get_size()
        self.cooking_book = pygame.transform.scale(original_cooking_book, (original_width * 5.5, original_height * 5.5))
        self.cooking_book_rect = self.cooking_book.get_rect(center=(self.screen_width / 2, self.screen_width / 2))

        # Cook Button
        self.cook_button_default = pygame.image.load("../assets/sprites/ui/cooking/button_cook_default.png").convert_alpha()
        self.cook_button_hover = pygame.image.load("../assets/sprites/ui/cooking/button_cook_hover.png").convert_alpha()
        self.cook_button_clicked = pygame.image.load("../assets/sprites/ui/cooking/button_cook_clicked.png").convert_alpha()
        self.cook_buttons = [self.cook_button_default, self.cook_button_hover, self.cook_button_clicked]
        self.cook_button_index = 0
        cook_button_x = self.cooking_book_rect.right - 50
        cook_button_y = self.cooking_book_rect.bottom - 50
        self.cook_button_rect = self.cook_button_default.get_rect(bottomright=(cook_button_x, cook_button_y))

    def button_cook(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = mouse_tracker.get_just_pressed()[0]
        if self.cook_button_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                self.screen.blit(self.cook_buttons[2], self.cook_button_rect)
                return True
            else:
                self.screen.blit(self.cook_buttons[1], self.cook_button_rect)
        else:
            self.screen.blit(self.cook_buttons[0], self.cook_button_rect)

        return False

    def book(self):
        self.screen.blit(self.cooking_book, self.cooking_book_rect)
        recipe_index = 0
        button_pressed = self.button_cook()
        if button_pressed:
            if not cook(self.inventory, recipe_index):
                return False
        return True
