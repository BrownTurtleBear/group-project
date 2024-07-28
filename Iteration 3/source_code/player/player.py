import pygame
from os import walk


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, colour):
        pygame.sprite.Sprite.__init__(self)
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.FACING = "right"
        self.image = ".../assets/sprites/ui/icon.png"
        self.rect = self.image.get_rect()
        self.position, self.velocity = pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move_left_right(1)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move_left_right(-1)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move_up_down(1)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move_up_down(-1)
        else:
            self.move_left_right(0)

    def move_left_right(self, key_walk=0):
        if key_walk == 0:
            """Deceleration scripts"""
            self.direction.x *= 0.8 # for ice physics make it 0.99
            if abs(self.direction.x) < 0.1:
                self.direction.x = 0
            return None
        top_speed = 1
        if abs(self.direction.x) >= top_speed:
            self.direction.x = top_speed * key_walk
        else:
            if self.direction.x == 0:
                self.direction.x = 0.3
            self.direction.x = self.direction.x + key_walk * 1.3
        self.facing_right = True if key_walk == 1 else False

    def move_up_down(self, key_walk=0):
        if key_walk == 0:
            """Deceleration scripts"""
            self.direction.x *= 0.8 # for ice physics make it 0.99
            if abs(self.direction.x) < 0.1:
                self.direction.x = 0
            return None
        top_speed = 1
        if abs(self.direction.x) >= top_speed:
            self.direction.x = top_speed * key_walk
        else:
            if self.direction.x == 0:
                self.direction.x = 0.3
            self.direction.x = self.direction.x + key_walk * 1.3
        self.facing_right = True if key_walk == 1 else False

    def update(self, screen, tile_size):
        self.get_input()
        self.animate()
        self.teleport(screen)
