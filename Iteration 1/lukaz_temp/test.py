from ui import UI
import pygame
from sys import exit

pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((400, 400))
pygame.display.set_icon(pygame.image.load('../assets/ui/menu/icon.png'))
clock = pygame.time.Clock()
clicked = ["main", False]
ui = UI(screen, clicked)
x, y = 10, 10
volume = 50

while True:
    screen.fill('black')
    w, h = screen_width - (x * 2), screen_height - (x * 2)
    pygame.draw.rect(screen, "White", pygame.Rect(x, y, w, h))
    if clicked[0] == "main":
        pos = pygame.mouse.get_pos()
        ui.text(screen_width/2, 60, 50, "Black", "Fishing Sim")
        exit_button = ui.button(screen_width - 70, 10, 60, 30, "Red", "exit")
        ui.text(screen.get_width()-39, 24, 15, "Black", "Exit")
        start_button = ui.button(screen_width / 2 - 80, screen_height / 2 - 90, 170, 80, "Green", "start")
        ui.text(screen_width / 2 + 5, screen_height / 2 - 50, 35, "Black", "Start")
        character_button = ui.button(screen_width / 2 - 80, screen_height / 2, 170, 80, "Blue", "character")
        ui.text(screen_width / 2 + 5, screen_height / 2 + 40, 35, "White", "Character")
        settings_button = ui.button(screen_width / 2 - 80, screen_height / 2 + 90, 170, 80, "Grey", "settings")
        ui.text(screen_width / 2 + 5, screen_height / 2 + 130, 35, "Black", "Settings")
    if clicked[0] == "settings":
        pygame.draw.rect(screen, "Grey", pygame.Rect(x, y, screen_width - (x * 2), screen_height - (x * 2)))
        ui.text(screen_width / 2, 60, 50, "Black", "Settings Menu")
        pygame.draw.rect(screen, "White",
                         pygame.Rect(screen_width / 6, screen_height / 4, screen_width / 3, screen_height / 2))
        ui.text(screen_width / 3, screen_height / 3 - 10, 25, "Black", "Volume")
        ui.text(screen_width / 4 + 35, screen_height / 2 + 10, 25, "Black", str(volume))
        ui.img_button(90, 210, 50, 45, '../assets/ui/menu/volume.png')
        up_button = ui.img_button(135, 160, 45, 45, '../assets/ui/menu/arrow.png')
        down_button = ui.img_button(135, 260, 45, 45, '../assets/ui/menu/arrow.png')
        exit_button = ui.button(screen_width - 70, 10, 60, 30, "Red", "main")
        ui.text(screen_width - 39, 24, 15, "Black", "Exit")
    if clicked[0] == "exit":
        pygame.quit()
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    clock.tick(60)
