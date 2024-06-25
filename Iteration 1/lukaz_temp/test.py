from ui import UI
import pygame

pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((400, 400))
pygame.display.set_icon(pygame.image.load('../assets/ui/menu/icon.png'))
clock = pygame.time.Clock()
clicked = ["main", False]
ui = UI(screen, clicked)
x, y = 10, 10

while True:
    screen.fill('black')
    w, h = screen_width - (x * 2), screen_height - (x * 2)
    pygame.draw.rect(screen, "White", pygame.Rect(x, y, w, h))
    if clicked[0] == "main":
        pos = pygame.mouse.get_pos()
        ui.text(screen_width/2, 60, 50, "Black", "Zesty Sim")
        exit_button = ui.button(screen_width - 70, 10, 60, 30, "Red")
        ui.text(screen.get_width()-39, 24, 15, "Black", "Exit")
        start_button = ui.button(screen_width / 2 - 80, screen_height / 2 - 90, 170, 80, "Green")
        ui.text(screen_width / 2 + 5, screen_height / 2 - 50, 35, "Black", "Start")
        character_button = ui.button(screen_width / 2 - 80, screen_height / 2, 170, 80, "Blue")
        ui.text(screen_width / 2 + 5, screen_height / 2 + 40, 35, "White", "Character")
        settings_button = ui.button(screen_width / 2 - 80, screen_height / 2 + 90, 170, 80, "Grey")
        ui.text(screen_width / 2 + 5, screen_height / 2 + 130, 35, "Black", "Settings")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    clock.tick(60)
