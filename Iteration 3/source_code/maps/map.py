import pygame
from pytmx.util_pygame import load_pygame
from players.player import Player

class Map:
    def __init__(self, filename, tile_size, screen):
        self.tmx_data = load_pygame(filename)
        self.width = 50
        self.height = 50
        self.tile_size = tile_size
        self.screen = screen
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.player_group = None
        self.player = Player((self.tile_size[0]*5, self.tile_size[1]*5), (self.tile_size[0]*2, self.tile_size[1]*2))
        self.load_sprites()

    def horizontal_movement_collision(self):
        player = self.player
        player.rect.x += player.direction.x * player.speed

        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite

        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.falling = 0
                    player.jump_height = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        if player.falling < 0 and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def load_sprites(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                for l in range(0, 2):
                    gid = self.tmx_data.get_tile_gid(i, j, l)
                    if gid:
                        img = self.tmx_data.get_tile_image_by_gid(gid)
                        sprite = pygame.sprite.Sprite()
                        sprite.image = img
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = i * self.tile_size[0]
                        sprite.rect.y = j * self.tile_size[0]
                        self.all_sprites.add(sprite)
                        if l == 1:
                            self.collision_sprites.add(sprite)
        # Player
        self.player_group = pygame.sprite.GroupSingle()
        x = 5 * self.tile_size[0]
        y = 5 * self.tile_size[1]
        player_sprite = Player((x, y), (self.tile_size[0]*2, self.tile_size[1]*2))
        self.player_group.add(player_sprite)

    def redraw(self):
        for i in range(self.width):
            for j in range(self.height):
                for l in range(0, 2):
                    gid = self.tmx_data.get_tile_gid(i, j, l)
                    if gid:
                        img = self.tmx_data.get_tile_image_by_gid(gid)
                        self.screen.blit(img, (i * self.tile_size[0], j * self.tile_size[0]))

    def run(self):
        self.redraw()
        self.player.update(self.screen)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
