import pygame
from os import walk


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, player_size):
        pygame.sprite.Sprite.__init__(self)
        self.facing = "right"
        self.sprite = pygame.image.load("../assets/sprites/ui/icon.png").convert_alpha()
        self.image = pygame.transform.scale(self.sprite, player_size)
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(pos)
        self.speed = 1.3

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move_left_right(1)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move_left_right(-1)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move_up_down(1)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move_up_down(-1)
        if keys[pygame.K_LSHIFT]:
            if self.speed < 2.6:
                self.speed += 0.1
        else:
            if self.speed > 1.3:
                self.speed -= 0.1

    def move_left_right(self, key_walk=0):
        self.position.x += key_walk * self.speed
        self.facing = "right" if key_walk == 1 else "left"

    def move_up_down(self, key_walk=0):
        self.position.y += key_walk * self.speed
        self.facing = "down" if key_walk == 1 else "up"

    def animate(self, screen):
        if self.facing == "up":
            player_im = pygame.transform.flip(self.image, False, True)
        # elif self.facing == "down":
            # player_im = pygame.transform.flip(self.image, True, True)
        elif self.facing == "right":
            player_im = pygame.transform.flip(self.image, True, False)
        else:
            player_im = self.image
        self.image_rect = self.position
        screen.blit(player_im, self.image_rect)

    def update(self, screen):
        self.get_input()
        self.animate(screen)
