import pygame

class Inventory:
    def __init__(self):
        self.items = {}
        self.image = pygame.image.load(r"Iteration 1\assets\sprites\items\inventory.png").convert_alpha()
        self.image_rect = self.image.get_rect(center=(0, 0))

    def add_item(self, item_name, quantity) -> None:
        found = False
        for item in self.items.keys():
            if item.name == item_name:
                self.items[item].amount += quantity
                found = True
                break
        if not found:
            self.items[item_name] = quantity

    def remove_item(self, item_name: str, quantity: int) -> None:
        for item in self.items.keys():
            if item.name == item_name:
                self.items[item] -= quantity
                if self.items[item] <= 0:
                    self.items.pop(item)
                    break
    
    def open(self, screen):
        screen.blit(self.image, self.image_rect)
        for items in self.items:
            print("yes")