import pygame
from pytmx.util_pygame import load_pygame


class Map:
    def __init__(self, filename, tilesize, screen):
        self.tmx_data = load_pygame(filename)
        self.width = 30
        self.height = 20
        self.tilesize = tilesize
        self.screen = screen
        self.load_sprites()

    def load_sprites(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                for l in range(0, 1 ):
                    gid = self.tmx_data.get_tile_gid(i, j, l)
                    if gid:
                        img = self.tmx_data.get_tile_image_by_gid(gid)
                        sprite = pygame.sprite.Sprite()
                        sprite.image = img
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = i * self.tilesize
                        sprite.rect.y = j * self.tilesize

    def redraw(self):
        for i in range(self.width):
            for j in range(self.height):
                for l in range(0, 2):
                    gid = self.tmx_data.get_tile_gid(i, j, l)
                    if gid:
                        img = self.tmx_data.get_tile_image_by_gid(gid)
                        self.screen.blit(img, (i * self.tilesize, j * self.tilesize))
