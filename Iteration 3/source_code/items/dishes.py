import pygame


class Dish:
    def __init__(self, name, pos, description=None):
        self.name = name
        self.pos = pos
        self.description = description
        self.image = pygame.image.load('../assets/sprites/items/food.png').convert_alpha()
