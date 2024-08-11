import pygame


class NPC(pygame.sprite.Sprite):
    def __init__(self, pos, size, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.sprite, size)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, screen):
        screen.blit(self.image, self.image_rect)
