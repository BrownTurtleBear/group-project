from interactions.ui import UI
from cooking.cooking import Cooking
from cooking.recipe import Recipe
from items.item import Item
from items.inventory import Inventory
from map.map import Map
from controls.key_tracker import KeyTracker
from controls.mouse_tracker import MouseTracker
from player.player import Player

import pygame
import math

pygame.init()
tile_size = (16, 16)
tiles_amount = (50, 50)
screen_width, screen_height = tile_size[0] * tiles_amount[0], tile_size[1] * tiles_amount[1]
sc_w, sc_h = 800, 600
screen = pygame.display.set_mode((sc_w, sc_h))
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
cooking = Cooking(screen, sc_w, inventory, mouse_tracker)
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
    w, h = sc_w - (x * 2), sc_h - (x * 2)
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
            if cookbook_open:
                cooking.book()
            current_map.redraw()
            player.
    if menu_section == "main":
        exit_button = ui.button("rect", False, sc_w * 0.825, sc_h * 0.025, sc_w * 0.15, sc_h * 0.075, "Red", None)
        start_button = ui.button("rect", False, sc_w * 0.3, sc_h * 0.275, sc_w * 0.425, sc_h * 0.2, "Green", None)
        character_button = ui.button("rect", False, sc_w * 0.3, sc_h * 0.5, sc_w * 0.425, sc_h * 0.2, "Blue", None)
        settings_button = ui.button("rect", False, sc_w * 0.3, sc_h * 0.725, sc_w * 0.425, sc_h * 0.2, "Grey", None)
        ui.text(sc_w * 0.5, sc_h * 0.15, int(sc_h * 0.15), "Black", "Love Bites")
        ui.text(sc_w * 0.9, sc_h * 0.06, int(sc_w * 0.04), "Black", "Exit")
        ui.text(sc_w * 0.5125, sc_h * 0.375, int(sc_h * 0.09), "Black", "Start")
        ui.text(sc_w * 0.5125, sc_h * 0.6, int(sc_h * 0.09), "White", "Character")
        ui.text(sc_w * 0.5125, sc_h * 0.825, int(sc_h * 0.09), "Black", "Settings")
        if exit_button:
            menu_section = "exit"
        if start_button:
            menu_section = "start"
        if character_button:
            menu_section = "character"
        if settings_button:
            menu_section = "settings"
    if menu_section == "settings":
        pygame.draw.rect(screen, "Grey", pygame.Rect(x, y, sc_w - (x * 2), sc_h - (x * 2)))
        ui.outlined_rect(sc_w / 6, sc_h / 4, sc_w / 3, sc_h / 2, 3, "White")
        ui.image(sc_w * 0.225, sc_h * 0.525, sc_w * 0.125, sc_h * 0.1125, '../assets/sprites/ui/volume.png')
        up_button = ui.button("img", True, sc_w * 0.3375, sc_h * 0.4, sc_h * 0.1125, sc_h * 0.1125, None,
                              '../assets/sprites/ui/arrow_up.png')
        down_button = ui.button("img", True, sc_w * 0.3375, sc_h * 0.65, sc_h * 0.1125, sc_h * 0.1125, None,
                                '../assets/sprites/ui/arrow_down.png')
        exit_button = ui.button("rect", False, sc_w * 0.825, sc_h * 0.025, sc_w * 0.15, sc_h * 0.075, "Red", None)
        ui.text(sc_w / 2, sc_h * 0.15, int(sc_h * 0.125), "Black", "Settings Menu")
        ui.text(sc_w / 3, sc_h / 3 - sc_h * 0.025, int(sc_w * 0.06), "Black", "Volume")
        ui.text(sc_w * 0.3375, sc_h / 2 + sc_h * 0.025, int(sc_w * 0.06), "Black", str(volume))
        ui.text(sc_w * 0.9, sc_h * 0.06, int(sc_w * 0.04), "Black", "Exit")
        if up_button and volume < 100:
            volume += 1
        if down_button and volume > 0:
            volume -= 1
        if exit_button:
            menu_section = "main"
    if menu_section == "character":
        pygame.draw.rect(screen, (3, 7, 252), pygame.Rect(x, y, sc_w - (x * 2), sc_h - (x * 2)))
        ui.outlined_rect(x * 2, sc_h * 0.5, sc_w - (x * 4), sc_h * 0.5 - (x * 2), 3, (200, 255, 255))
        ui.text(sc_w / 2, sc_h * 0.0875, int(sc_w * 0.075), "White", "Character Customisation")
        # Section Boxes
        for i, value in enumerate(ui.sprite_values.keys()):
            if ui.menu_option == value:
                button = ui.button("img", True, ((x * 2) + (sc_w * 0.0625) + (sc_w * 0.125 * i)), sc_h * 0.4,
                                   sc_w * 0.15, sc_w * 0.15, None, '../assets/sprites/ui/box1.png')
            else:
                if ui.button("img", True, ((x * 2) + (sc_w * 0.0625) + (sc_w * 0.125 * i)), sc_h * 0.4,
                             sc_w * 0.125, sc_w * 0.125, None, '../assets/sprites/ui/box1.png'):
                    ui.menu_option = value
        # Colour Boxes
        if ui.menu_option != "Gender":
            ui.outlined_rect(x * 3, sc_h * 0.58,
                             (sc_w - (x * 4)) * 0.5, sc_h * 0.4 - x * 2, 3, "White")
            ui.outlined_rect((sc_w - (x * 4) * 0.5) / 2 + 10, sc_h * 0.58,
                             (sc_w - (x * 4)) * 0.5 - 10, sc_h / 2.5 - x * 2, 3, "White")
            # Menu Text
            ui.text(sc_w / 2, sc_h / 2 + sc_h * 0.04, int(sc_h * 0.0625), "Black", ui.menu_option)
            ui.text((sc_w - (x * 4) * 0.5) / 4, sc_h * 0.6 + sc_h * 0.025, int(sc_h * 0.05), "Black", "Style")
            ui.text((sc_w - (x * 4) * 0.6) * 0.75, sc_h * 0.6 + 10, int(sc_h * 0.05), "Black", "Colour")
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
                colour_button = ui.button("rect", False, (sc_w - (x * 4) * 0.5) / 1.8 + ((sc_w * 0.0625) * x_temp),
                                          sc_h * 0.7 + ((sc_w * 0.0625) * y_temp), x * (sc_w * 0.005), y * (sc_w * 0.005), value, None)
                if colour_button:
                    ui.sprite_values[ui.menu_option][0] = value
        else:
            ui.outlined_rect(x * 3, sc_h * 0.58, (sc_w - (x * 6)), sc_h / 2.5 - x * 2, 3, "White")
            ui.text(sc_w / 2, sc_h / 2 + sc_h * 0.04, int(sc_h * 0.0625), "Black", ui.menu_option)
            genders = ["Male", "Female", "None"]
            for i, value in enumerate(genders):
                ui.text(sc_w * 0.2, sc_h * 0.7, int(sc_h * 0.0625), "Black", "Male")
                ui.text(sc_w * 0.5, sc_h * 0.7, int(sc_h * 0.0625), "Black", "Female")
                ui.text(sc_w * 0.8, sc_h * 0.7, int(sc_h * 0.0625), "Black", "None")
                # Buttons
                if ui.sprite_values["Gender"] == value:
                    gender_button = ui.button("rect", False, sc_w * 0.125 + (sc_w * 0.3 * i), sc_h * 0.75, sc_w / 6,
                                              sc_h / 8 - sc_h * 0.025, "Green", None)

                else:
                    gender_button = ui.button("rect", False, sc_w * 0.125 + (sc_w * 0.3 * i), sc_h * 0.75, sc_w / 6,
                                              sc_h / 8 - sc_h * 0.025, "Red", None)
                ui.text(sc_w * 0.2 + (sc_w * 0.3 * i), sc_h * 0.8, int(sc_h * 0.0625), "Black", "Pick")
                if gender_button:
                    ui.sprite_values["Gender"] = value
        exit_button = ui.button("rect", False, sc_w * 0.8, sc_h * 0.15, sc_w * 0.15, sc_h * 0.075, "Red", None)
        if exit_button:
            menu_section = "main"
        ui.text(sc_w * 0.875, sc_h * 0.185, int(sc_w * 0.04), "Black", "Exit")
    if menu_section == "exit":
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(60)

pygame.quit()
