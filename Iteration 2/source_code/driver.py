from interactions.ui import UI
from cooking.cooking import Cooking
from cooking.recipe import Recipe
from items.item import Item
from items.inventory import Inventory
from map.map import Map
from controls.key_tracker import KeyTracker
from controls.mouse_tracker import MouseTracker

import pygame
import math

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(pygame.image.load('../assets/sprites/ui/icon.png'))
pygame.display.set_caption("Love Bites")
clock = pygame.time.Clock()
menu_section = "main"
playing = False
x, y = 10, 10
volume = 50

# Classes
ui = UI(screen)
inventory = Inventory()
current_map = Map("../assets/sprites/tile/map1.tmx", 16, screen)
key_tracker = KeyTracker()
mouse_tracker = MouseTracker()
cooking = Cooking(screen, screen_width, inventory, mouse_tracker)
# Items and Inventory
items = {
    "Egg": Item("Egg", (0, 2), (40, 60), "Just an egg."),
    "Bread": Item("Bread", (2, 3), (30, 40), "One loaf."),
}
recipes = {
    "Fried Egg on Toast": Recipe("Fried Egg on Toast", [items["Egg"], items["Bread"]], "Just egg on toast.")
}
inventory.add_recipe(recipes["Fried Egg on Toast"])
inventory_open = False
cookbook_open = False

mouse_released = None

running = True
while running:
    screen.fill('black')
    w, h = screen_width - (x * 2), screen_height - (x * 2)
    pygame.draw.rect(screen, "White", pygame.Rect(x, y, w, h))
    if menu_section == "start":
        if not playing:
            playing = True
        else:
            pos = pygame.mouse.get_pos()
            key_tracker.update()
            if KeyTracker.K_e in key_tracker.keys_just_pressed():
                if cookbook_open:
                    cookbook_open = False
                inventory_open = not inventory_open
            elif KeyTracker.K_r in key_tracker.keys_just_pressed():
                if inventory_open:
                    inventory_open = False
                cookbook_open = not cookbook_open
            if inventory_open:
                inventory.open(screen)
                if pygame.mouse.get_pressed()[0] == 1:
                    mouse_x, mouse_y = pos
                    new_position = (mouse_x - inventory.image_rect.x, mouse_y - inventory.image_rect.y)
                    inventory.move_item("Egg", new_position)
            if cookbook_open:
                cooking.book()
    if menu_section == "main":
        exit_button = ui.button("rect", False, screen_width - 70, 10, 60, 30, "Red", None)
        start_button = ui.button("rect", False, screen_width / 2 - 80, screen_height / 2 - 90, 170, 80, "Green", None)
        character_button = ui.button("rect", False, screen_width / 2 - 80, screen_height / 2, 170, 80, "Blue", None)
        settings_button = ui.button("rect", False, screen_width / 2 - 80, screen_height / 2 + 90, 170, 80, "Grey", None)
        ui.text(screen_width / 2, 60, 50, "Black", "Love Bites")
        ui.text(screen_width - 39, 24, 15, "Black", "Exit")
        ui.text(screen_width / 2 + 5, screen_height / 2 - 50, 35, "Black", "Start")
        ui.text(screen_width / 2 + 5, screen_height / 2 + 40, 35, "White", "Character")
        ui.text(screen_width / 2 + 5, screen_height / 2 + 130, 35, "Black", "Settings")
        if exit_button:
            menu_section = "exit"
        if start_button:
            menu_section = "start"
        if character_button:
            menu_section = "character"
        if settings_button:
            menu_section = "settings"
    if menu_section == "settings":
        pygame.draw.rect(screen, "Grey", pygame.Rect(x, y, screen_width - (x * 2), screen_height - (x * 2)))
        ui.outlined_rect(screen_width / 6, screen_height / 4, screen_width / 3, screen_height / 2, 3, "White")
        ui.image(90, 210, 50, 45, '../assets/sprites/ui/volume.png')
        up_button = ui.button("img", True, 135, 160, 45, 45, None, '../assets/sprites/ui/arrow_up.png')
        down_button = ui.button("img", True, 135, 260, 45, 45, None, '../assets/sprites/ui/arrow_down.png')
        exit_button = ui.button("rect", False, screen_width - 70, 10, 60, 30, "Red", None)
        ui.text(screen_width / 2, 60, 50, "Black", "Settings Menu")
        ui.text(screen_width / 3, screen_height / 3 - 10, 25, "Black", "Volume")
        ui.text(screen_width / 4 + 35, screen_height / 2 + 10, 25, "Black", str(volume))
        ui.text(screen_width - 39, 24, 15, "Black", "Exit")
        if up_button and volume < 100:
            volume += 1
        if down_button and volume > 0:
            volume -= 1
        if exit_button:
            menu_section = "main"
    if menu_section == "character":
        pygame.draw.rect(screen, (3, 7, 252), pygame.Rect(x, y, screen_width - (x * 2), screen_height - (x * 2)))
        ui.outlined_rect(x * 2, screen_height * 0.5, screen_width - (x * 4), screen_height * 0.45, 3, (200, 255, 255))
        ui.text(screen_width / 2, 35, 30, "White", "Character Customisation")
        # Section Boxes
        for i, value in enumerate(ui.sprite_values.keys()):
            if ui.menu_option == value:
                button = ui.button("img", True, (x * 2) + (50 / 2) + (50 * i), 175, 60, 60, None,
                                   '../assets/sprites/ui/box1.png')
            else:
                if ui.button("img", True, (x * 2) + (50 / 2) + (50 * i), 175, 50, 50, None,
                             '../assets/sprites/ui/box1.png'):
                    ui.menu_option = value
        # Colour Boxes
        if ui.menu_option != "Gender":
            ui.outlined_rect(x * 3, screen_height * 0.58,
                             (screen_width - (x * 4)) * 0.5, screen_height / 2.5 - x * 2, 3, "White")
            ui.outlined_rect((screen_width - (x * 4) * 0.5) / 2 + 10, screen_height * 0.58,
                             (screen_width - (x * 4)) * 0.5 - 10, screen_height / 2.5 - x * 2, 3, "White")
            # Menu Text
            ui.text(screen_width / 2, screen_height / 2 + 15, 25, "Black", ui.menu_option)
            ui.text((screen_width - (x * 4) * 0.5) / 4 + 20, screen_height * 0.6 + 10, 20, "Black", "Style")
            ui.text((screen_width - (x * 4) * 0.6) * 0.75, screen_height * 0.6 + 10, 20, "Black", "Colour")
            for i, value in enumerate(ui.colours_dict[ui.menu_option]):
                if i - 6 < 0:
                    x_temp = i
                else:
                    x_temp = i - 6
                y_temp = math.floor(i / 6)
                if value == "Black":
                    temp1 = "Grey"
                else:
                    temp1 = "Black"
                colour_button = ui.button("rect", False, (screen_width - (x * 4) * 0.5) / 1.8 + (25 * x_temp),
                                          screen_height * 0.7 + (25 * y_temp), x * 2, y * 2, value, None)
                if colour_button:
                    ui.sprite_values[ui.menu_option][0] = value
        else:
            ui.outlined_rect(x * 3, screen_height * 0.58, (screen_width - (x * 6)), screen_height / 2.5 - x * 2, 3,
                             "White")
            ui.text(screen_width / 2, screen_height / 2 + 15, 25, "Black", ui.menu_option)
            genders = ["Male", "Female", "None"]
            for i, value in enumerate(genders):
                ui.text(screen_width * 0.2, screen_height * 0.7, 25, "Black", "Male")
                ui.text(screen_width * 0.5, screen_height * 0.7, 25, "Black", "Female")
                ui.text(screen_width * 0.8, screen_height * 0.7, 25, "Black", "None")
                # Buttons
                if ui.sprite_values["Gender"] == value:
                    gender_button = ui.button("rect", False, 50 + (120 * i), screen_height * 0.75, screen_width / 6,
                                              screen_height / 8 - 10, "Green", None)

                else:
                    gender_button = ui.button("rect", False, 50 + (120 * i), screen_height * 0.75, screen_width / 6,
                                              screen_height / 8 - 10, "Red", None)
                ui.text(screen_width * 0.2 + (120 * i), screen_height * 0.8, 25, "Black", "Pick")
                if gender_button:
                    ui.sprite_values["Gender"] = value
        exit_button = ui.button("rect", False, screen_width * 0.8, 60, 60, 30, "Red", None)
        if exit_button:
            menu_section = "main"
        ui.text(screen_width * 0.875, 74, 15, "Black", "Exit")
    if menu_section == "exit":
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(60)

pygame.quit()
