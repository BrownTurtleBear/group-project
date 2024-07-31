import pygame
from interactions.ui import UI


def cook(inventory, recipe):
    needed_ingredients = inventory.recipes[recipe].ingredients
    if all(ni in inventory.items for ni in needed_ingredients):
        return True
    else:
        return False


class Cooking:
    def __init__(self, screen, inventory):
        self.screen = screen
        self.inventory = inventory
        self.ui = UI(self.screen)
        self.recipe_index = 0

        # Book
        original_cooking_book = pygame.image.load("../assets/sprites/ui/cooking/book.png").convert()
        original_width, original_height = original_cooking_book.get_size()
        self.cooking_book = pygame.transform.scale(original_cooking_book, (original_width * 5, original_height * 5))
        self.cooking_book_rect = self.cooking_book.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2))

    def book(self):
        self.screen.blit(self.cooking_book, self.cooking_book_rect)

        #cook button
        cook_pressed = self.ui.better_image_button("cook", "bottomright", self.cooking_book_rect.right - 85,
                                                   self.cooking_book_rect.bottom - 130)
        if cook_pressed and cook(self.inventory, self.recipe_index):
            print(f"cooked {self.inventory.recipes[self.recipe_index].name}")
        elif cook_pressed and not cook(self.inventory, self.recipe_index):
            print(f"You cant cook {self.inventory.recipes[self.recipe_index].name}")

        #next button
        next_pressed = self.ui.better_image_button("next", "bottomright", self.cooking_book_rect.right - 50,
                                                   self.cooking_book_rect.bottom - 50)
        if next_pressed:
            if self.recipe_index == len(self.inventory.recipes) - 1:
                self.recipe_index = 0
            else:
                self.recipe_index += 1

        self.ui.better_text("center", self.cooking_book_rect.left + 160, self.cooking_book_rect.top + 60, 26, "Black", self.inventory.recipes[self.recipe_index].name)
        self.ui.better_text("topright", self.cooking_book_rect.left + 220, self.cooking_book_rect.bottom - 220, 20, "Black", self.inventory.recipes[self.recipe_index].description)
