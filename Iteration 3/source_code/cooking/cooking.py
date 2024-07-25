import pygame
from interactions.ui import UI

def cook(inventory, recipe):
    needed_ingredients = inventory.recipes[recipe]
    if all(ni in inventory for ni in needed_ingredients):
        return True
    else:
        return False


class Cooking:
    def __init__(self, screen, inventory):
        self.screen = screen
        self.inventory = inventory
        self.ui = UI(self.screen)

        # Book
        original_cooking_book = pygame.image.load("../assets/sprites/ui/cooking/book.png").convert()
        original_width, original_height = original_cooking_book.get_size()
        self.cooking_book = pygame.transform.scale(original_cooking_book, (original_width * 5, original_height * 5))
        self.cooking_book_rect = self.cooking_book.get_rect(center=(self.screen.width / 2, self.screen.height / 2))

    def book(self):
        self.screen.blit(self.cooking_book, self.cooking_book_rect)
        recipe_index = 0
        cook_pressed = self.ui.better_image_button("cook", "bottomright", self.cooking_book_rect.right - 85, self.cooking_book_rect.bottom - 130)
        if cook_pressed and cook(self.inventory, recipe_index):
            print(f"cooked {self.inventory.recipes[recipe_index].name}")
            return True
        else:
            return False
