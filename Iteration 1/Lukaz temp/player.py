import pygame
from os import walk


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, colour):
        super().__init__()
        self.import_character_assets(colour)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # Player Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3

        # Player Status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False

    def import_folder(self, path):
        surface_list = []
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = path + "/" + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
        return surface_list

    def import_character_assets(self, colour):
        character_path = ('Sprites/Player/' + colour + '/')
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': [], 'land': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = self.import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # Loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def get_input(self, x_spawn, y_spawn, tile_size):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move_left_right(1)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move_left_right(-1)
        else:
            self.move_left_right(0)
        if keys[pygame.K_r]:
            self.rect.x = x_spawn * tile_size
            self.rect.y = y_spawn * tile_size

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

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 5:
            self.status = 'fall'
        elif self.direction.y > 1.6:
            self.status = 'land'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def teleport(self, screen):
        sc_width, sc_height = screen.get_size()
        if self.rect.y > sc_height-2:
            x_pos = self.rect.x
            self.rect.y = 1
            self.rect.x = x_pos
        if self.rect.y <= 0:
            x_pos = self.rect.x
            self.rect.y = sc_height - 2
            self.rect.x = x_pos
        if self.rect.x > sc_width-2:
            y_pos = self.rect.y
            self.rect.x = 1
            self.rect.y = y_pos
        if self.rect.x <= 0:
            y_pos = self.rect.y
            self.rect.x = sc_width - 2
            self.rect.y = y_pos

    def update(self, screen, x_spawn, y_spawn, tile_size):
        self.get_input(x_spawn, y_spawn, tile_size)
        self.get_status()
        self.animate()
        self.teleport(screen)
