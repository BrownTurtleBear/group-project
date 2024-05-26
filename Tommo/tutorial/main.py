import pygame
from sys import exit

# General setup
pygame.init( )

# Game Screen
screen_width = 800
screen_height= 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gaym')

# For Frame rate
clock = pygame.time.Clock()

# box
# test_surface = pygame.Surface((screen_width, 100))
# test_surface.fill('Yellow')

# image
test_surface = pygame.image.load("graphics/Sky.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # drawing elements
    screen.blit(test_surface, (0, (screen_height - 100)))

    # update everything
    pygame.display.update()
    clock.tick(60) # 60 fps