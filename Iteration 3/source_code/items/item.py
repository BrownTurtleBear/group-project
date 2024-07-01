import pygame


class Item:
    def __init__(self, name, pos, inventory_pos, description=None):
        self.name = name
        self.pos = pos
        self.inventory_pos = inventory_pos
        self.description = description
        self.image = pygame.image.load('../Assets/Sprites/Items/food.png').convert_alpha()
    