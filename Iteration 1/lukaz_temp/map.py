import pygame
from pytmx.util_pygame import load_pygame
from bs4 import BeautifulSoup
from lukaz_temp.player import Player


class Map:
    def __init__(self, filename, tile_size, height, width, level_on):
        # Create Level
        #self.screen = pygame.display.set_mode((height*tile_size, width*tile_size))
        self.tmx_data = load_pygame(filename)
        with open(filename, 'r') as f:
            data = f.read()
        self.height = height
        self.width = width
        self.tile_size = tile_size
        self.allsprites = pygame.sprite.Group()
        self.wallsprites = pygame.sprite.Group()
        self.spawnPoints = [(1, 1), (46, 12), (2, 4), (2, 3), (1, 11), (1, 1)]
        self.spawnPointX, self.spawnPointY = self.spawnPoints[level_on][0], self.spawnPoints[level_on][1]

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.wallsprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.rect.y += player.direction.y * player.speed

        for sprite in self.wallsprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top

    def load_sprites(self, colour):
        # Tile Sprites
        for i in range(0, self.width):
            for j in range(0, self.height):
                for l in range(0, 1):
                    gid = self.tmx_data.get_tile_gid(i, j, l)
                    if gid:
                        img = self.tmx_data.get_tile_image_by_gid(gid)
                        sprite = pygame.sprite.Sprite()
                        sprite.image = img
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = i * self.tile_size
                        sprite.rect.x = i * self.tile_size
                        sprite.rect.y = j * self.tile_size
                        self.allsprites.add(sprite)
                        if l == 0:
                            self.wallsprites.add(sprite)
        # Player
        self.player = pygame.sprite.GroupSingle()
        x = self.spawnPointX * self.tile_size
        y = self.spawnPointY * self.tile_size
        player_sprite = Player((x, y), colour)
        self.player.add(player_sprite)

    def redraw(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                for l in range(0, 1):
                    gid = self.tmx_data.get_tile_gid(i, j, l)
                    if gid:
                        img = self.tmx_data.get_tile_image_by_gid(gid)
                        self.screen.blit(img, (i * self.tile_size, j * self.tile_size))

    def run(self):
        # Level Tiles
        self.redraw()
        # Player
        self.player.update(self.screen, self.spawnPointX, self.spawnPointY, self.tile_size)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.screen)
