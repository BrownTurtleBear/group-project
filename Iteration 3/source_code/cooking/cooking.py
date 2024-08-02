import pygame
from interactions.button import Button
from interactions.ui import UI


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
                                  self.cooking_book_rect.right - 235, self.cooking_book_rect.bottom - 200, 0.9, 0.9)
        self.next_button = Button(self.screen, "cooking", "next", "bottomright",
                                  self.cooking_book_rect.right - 120, self.cooking_book_rect.bottom - 90, 0.45, 0.45)

        self.buttons = [self.cook_button, self.next_button]

        self.show_cooked_text = False
        self.cook_text_timer = 0
        self.cooked_recipe_name = ""

    def cook(self, recipe):
        needed_ingredients = self.inventory.recipes[recipe].ingredients
        for ingredient in needed_ingredients:
            if ingredient.name not in self.inventory.items or self.inventory.items[ingredient.name]['quantity'] == 0:
                self.show_cooked_text = False
                self.cook_text_timer = pygame.time.get_ticks()
                self.cooked_recipe_name = self.inventory.recipes[recipe].name
                return False

        self.inventory.add_dish(self.inventory.recipes[recipe].dish, 1)
        for ingredient in needed_ingredients:
            self.inventory.remove_item(ingredient, 1)

        self.show_cooked_text = True
        self.cook_text_timer = pygame.time.get_ticks()
        self.cooked_recipe_name = self.inventory.recipes[recipe].name
        return True

    def update_cooked_text(self):
        current_time = pygame.time.get_ticks()
        time_elapsed = current_time - self.cook_text_timer

        if time_elapsed <= 2000:
            text = f"Cooked {self.cooked_recipe_name}" if self.show_cooked_text else f"Could not cook {self.cooked_recipe_name}"
            self.ui.better_text("aller-font", "Aller_Bd", "center", self.screen.get_width() // 2,
                                self.screen.get_height() - 20, 20, "Black", text)
        else:
            self.show_cooked_text = False

    def book(self):
        self.screen.blit(self.cooking_book, self.cooking_book_rect)

        for button in self.buttons:
            button.update()
            button.draw()

        if self.cook_button.clicked:
            if self.cook(self.recipe_index):
                self.show_cooked_text = True
            else:
                self.show_cooked_text = False
            self.cook_text_timer = pygame.time.get_ticks()

        if self.next_button.clicked:
            self.recipe_index = (self.recipe_index + 1) % len(self.inventory.recipes)

        self.ui.better_text("aller-font", "Aller_Bd", "center", self.cooking_book_rect.left + 160,
                            self.cooking_book_rect.top + 60, 26, "Black",
                            self.inventory.recipes[self.recipe_index].name)
        self.ui.better_text("aller-font", "Aller_Bd", "topright", self.cooking_book_rect.left + 220,
                            self.cooking_book_rect.bottom - 220, 20,
                            "Black", self.inventory.recipes[self.recipe_index].description)

        self.update_cooked_text()
