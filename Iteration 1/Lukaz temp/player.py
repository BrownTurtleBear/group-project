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
        # player Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        # player Status
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
        character_path = ('sprites/player/' + colour + '/')
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
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move_left_right(-1)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move_up_down(-1)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move_up_down(1)
        else:
            self.move_left_right(0)
        if keys[pygame.K_r]:
            self.rect.x = x_spawn * tile_size
            self.rect.y = y_spawn * tile_size

    def move_left_right(self, key_walk=0):
        self.rect.x += key_walk

    def move_up_down(self, key_walk=0):
        self.rect.y += key_walk

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

    def update(self, screen, x_spawn, y_spawn, tile_size):
        self.get_input(x_spawn, y_spawn, tile_size)
        self.get_status()
        self.animate()
