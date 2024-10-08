import pygame


class Inventory:
    def __init__(self):
        self.image = pygame.image.load('../assets/sprites/items/inventory.png').convert_alpha()
        self.image_rect = self.image.get_rect()
        self.items = {}
        self.recipes = []

    def add_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name]['quantity'] += quantity
        else:
            self.items[item.name] = {'item': item, 'quantity': quantity}

    def add_recipe(self, recipe):
        if recipe in self.recipes:
            return False
        else:
            self.recipes.append(recipe)

    def open(self, screen):
        screen.blit(self.image, self.image_rect)
        for item_dict in self.items.values():
            item = item_dict['item']
            x, y = item.pos
            inv_x, inv_y = item.inventory_pos
            scaled_item_image = pygame.transform.scale(item.image, (item.image.get_width() * 2, item.image.get_height() * 2))
            item_rect = pygame.Rect(x * 32, y * 32, 32, 32)
            screen.blit(scaled_item_image, (self.image_rect.x + inv_x, self.image_rect.y + inv_y), item_rect)

    def move_item(self, item_name, new_position):
        if item_name in self.items:
            self.items[item_name]['item'].inventory_pos = new_position
