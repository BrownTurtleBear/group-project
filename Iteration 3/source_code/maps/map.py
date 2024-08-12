import pygame
from pytmx.util_pygame import load_pygame
from players.player import Player
from npcs.npc import NPC


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
        self.npc_group = pygame.sprite.Group()
        self.player = Player((self.tile_size[0]*5, self.tile_size[1]*5), (self.tile_size[0]*2, self.tile_size[1]*2))
        self.load_sprites()

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
        player_sprite = Player((50, 50), (self.tile_size[0]*2, self.tile_size[1]*2))
        self.player_group.add(player_sprite)

        # NPCs
        npc1 = NPC((100, 100), (self.tile_size[0]*2, self.tile_size[1]*2), "../assets/sprites/characters/red_miku.png")
        npc2 = NPC((200, 150), (self.tile_size[0]*2, self.tile_size[1]*2), "../assets/sprites/characters/yellow_miku.png")
        npc3 = NPC((300, 200), (self.tile_size[0]*2, self.tile_size[1]*2), "../assets/sprites/characters/purple_miku.png")
        self.npc_group.add(npc1, npc2, npc3)

        self.collision_sprites.add(npc1, npc2, npc3)

    # Note that 'collided' initialisation can't be factored as x & y can have separate collisions
    def x_collision(self):
        player = self.player
        collided = pygame.sprite.spritecollide(player, self.collision_sprites, False)
        if collided:
            if player.facing == "left": # If player is moving left
                player.rect.left = collided[0].rect.right
            elif player.facing == "right": # If player is moving right
                player.rect.right = collided[0].rect.left
            player.position.x = player.rect.x

    def y_collision(self):
        player = self.player
        collided = pygame.sprite.spritecollide(player, self.collision_sprites, False)
        if collided:
            if player.facing == "up": # If player is moving up
                player.rect.top = collided[0].rect.bottom
            elif player.facing == "down": # If player is moving down
                player.rect.bottom = collided[0].rect.top
            player.position.y = player.rect.y

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
        self.player.x_input()
        self.x_collision()
        self.player.y_input()
        self.y_collision()
        self.player.speed_input()
        self.player.animate(self.screen)
        for npc in self.npc_group:
            npc.update(self.screen)
