import pygame


class Item:
    def __init__(self, name, coords, inventory_pos, description=None):
        self.name = name
        self.coords = coords
        self.inventory_pos = inventory_pos
        self.description = description
        self.image = pygame.image.load(r"Iteration 1\assets\sprites\items\food.png").convert_alpha()
    