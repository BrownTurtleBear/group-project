import pygame

from sys import exit
from ui.cooking import Cooking
from items.item import Item
from items.inventory import Inventory

screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(pygame.image.load(r'.\assets\ui\menu\icon.png'))
pygame.display.set_caption("Love Bites")

clock = pygame.time.Clock()

pygame.init()

cooking = Cooking()

items = {
    "Egg": Item("Egg", (0, 2), (40, 60), "Just an egg."),
    "Bread": Item("Bread", (2, 3), (30, 40), "One loaf."),
}

inventory = Inventory()

inventory.add_item(items["Egg"], 1)
inventory.add_item(items["Bread"], 1)

inventory_open = False
cookbook_open = False

mouse_released = None

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inventory_open and event.button == 1:
                mouse_x, mouse_y = event.pos
                new_position = (mouse_x - inventory.image_rect.x, mouse_y - inventory.image_rect.y)
                inventory.move_item("Egg", new_position)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if cookbook_open:
                    cookbook_open = False
                inventory_open = not inventory_open
            if event.key == pygame.K_r:
                if inventory_open:
                    inventory_open = False
                cookbook_open = not cookbook_open
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_released = True

    if inventory_open:
        inventory.open(screen)

    if cookbook_open:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if cooking.open(screen, mouse_pos, mouse_pressed, mouse_released):
            success, cooked_food = cooking.cook(inventory.items, "Fried Egg on Toast")
            if success:
                inventory.add_item(cooked_food, 1)
                print(f"Successfully cooked {cooked_food}")
            else:
                print("Couldn't cook the recipe")

    mouse_released = False

    pygame.display.update()
    clock.tick(60)
