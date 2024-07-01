import pygame


class Item:
    def __init__(self, name, pos, inventory_pos, description=None):
        self.name = name
        self.pos = pos
        self.inventory_pos = inventory_pos
        self.description = description
        self.image = pygame.image.load(r"assets\sprites\items\food.png").convert_alpha()
    