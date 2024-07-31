import pygame
from interactions.button import Button
from controls.mouse_tracker import mouse_tracker
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
        self.recipe_index = 0
        self.ui = UI(self.screen)

        # Book
        original_cooking_book = pygame.image.load("../assets/sprites/ui/cooking/book.png").convert()
        original_width, original_height = original_cooking_book.get_size()
        self.cooking_book = pygame.transform.scale(original_cooking_book, (original_width * 5, original_height * 5))
        self.cooking_book_rect = self.cooking_book.get_rect(
            center=(self.screen.get_width() / 2, self.screen.get_height() / 2))

        # Create buttons
        self.cook_button = Button(self.screen, "cooking", "cook", "bottomright",
                                  self.cooking_book_rect.right - 85, self.cooking_book_rect.bottom - 130, 0.9, 0.9)
        self.next_button = Button(self.screen, "cooking", "next", "bottomright", self.cooking_book_rect.right - 50,
                                  self.cooking_book_rect.bottom - 50, 0.45, 0.45)

        self.buttons = [self.cook_button, self.next_button]

    def book(self):
        self.screen.blit(self.cooking_book, self.cooking_book_rect)

        for button in self.buttons:
            button.update(mouse_tracker)
            button.draw()

        if self.cook_button.clicked:
            if cook(self.inventory, self.recipe_index):
                print(f"cooked {self.inventory.recipes[self.recipe_index].name}")
            else:
                print(f"You can't cook {self.inventory.recipes[self.recipe_index].name}")

        if self.next_button.clicked:
            self.recipe_index = (self.recipe_index + 1) % len(self.inventory.recipes)

        self.ui.better_text("center", self.cooking_book_rect.left + 160, self.cooking_book_rect.top + 60, 26, "Black",
                            self.inventory.recipes[self.recipe_index].name)
        self.ui.better_text("topright", self.cooking_book_rect.left + 220, self.cooking_book_rect.bottom - 220, 20,
                            "Black", self.inventory.recipes[self.recipe_index].description)
