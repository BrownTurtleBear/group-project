import pygame, sys
import random
from player import Player
from map import Map
from ui import UI

pygame.init()
width = 20
height = 20
tile_size = 20
screen_width = width * tile_size
screen_height = height * tile_size
screen = pygame.display.set_mode((screen_height, screen_height))
pygame.display.set_caption("Fishing Sim")
pygame.display.set_icon(pygame.image.load('../assets/ui/menu/icon.png'))
clock = pygame.time.Clock()
x, y = 10, 1
clicked = ["main", False]
start = False
settings = False
character_custom = False

# Defining Classes
ui = UI(screen, clicked)
player1 = Player((1, 1), "Red")
mapping = Map(('../assets/levels/map' + str(1) + '.tmx'), tile_size, width, height, 1)

while True:
    screen.fill('black')
    w, h = screen_width - (x * 2), screen_height - (x * 2)
    pygame.draw.rect(screen, "White", pygame.Rect(x, y, w, h))
    if start:
        mapping.load_sprites("Red")
        mapping.run()
    elif character_custom:
        ui.customisation(x, y)
        if ui.exit == True:
            clicked[0] = "main"
            character_custom = False
            ui.exit = False
    elif settings:
        if ui.settings_menu(x, y) is not None:
            clicked[0], settings = ui.settings_menu(x, y)
    else:
        if clicked[0] == "settings":
            settings = True
        elif clicked[0] == "start":
            start = True
        elif clicked[0] == "character":
            character_custom = True
        else:
            clicked[0] = ui.main_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
