import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/sprites/player/mogus.png").convert_alpha()
        self.frame = 0
        
    def animate(self, frame, image):
        print("animate")

screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.K_SPACE:
            print("Jump")


    pygame.display.update()
    clock.tick(60)