import pygame
from sys import exit
from cooking import Cooking


screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

cooking = Cooking(r"Iteration 1\ui\recipes.json")

pygame.init()

cook_button_default = pygame.image.load(r"Iteration 1\assets\ui\cooking\button_cook_defaut.png").convert_alpha()
cook_button_hover = pygame.image.load(r"Iteration 1\assets\ui\cooking\button_hover.png").convert_alpha()
cook_button_clicked = pygame.image.load(r"Iteration 1\assets\ui\cooking\button_clicked.png").convert_alpha()
cook_button = [cook_button_default, cook_button_hover, cook_button_clicked]
cook_button_index = 0
cook_button_rect = cook_button_default.get_rect(center=(screen_width / 2, screen_height / 2)) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if event.type == pygame.MOUSEMOTION:
            if cook_button_rect.collidepoint(event.pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        cook_button_index = 2
                    else:
                        cook_button_index = 1
                    
                    items = ["apple", ""]
            else:
                cook_button_index = 0
                    
    screen.blit(cook_button[cook_button_index], cook_button_rect)

    pygame.display.update()
    clock.tick(60)