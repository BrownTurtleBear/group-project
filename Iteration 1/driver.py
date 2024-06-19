import pygame
from sys import exit
from ui.cooking import Cooking
from items.item import Item
from items.inventory import Inventory

screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

pygame.init()

# cooking = Cooking()

items = {
    "Egg": Item("Egg", (1, 3), (40, 60), "Just an egg."),
    "Bread": Item("Bread", (3, 4), (30, 40), "One loaf."),
}

inventory = Inventory()

inventory.add_item(items["Egg"], 1)
inventory.add_item(items["Bread"], 1)

cook_button_default = pygame.image.load(r"Iteration 1\assets\ui\cooking\button_cook_defaut.png").convert_alpha()
cook_button_hover = pygame.image.load(r"Iteration 1\assets\ui\cooking\button_cook_hover.png").convert_alpha()
cook_button_clicked = pygame.image.load(r"Iteration 1\assets\ui\cooking\button_cook_clicked.png").convert_alpha()
cook_button = [cook_button_default, cook_button_hover, cook_button_clicked]
cook_button_index = 0
cook_button_rect = cook_button_default.get_rect(center=(screen_width / 2, screen_height / 2)) 

HIDE_TEXT_EVENT = pygame.USEREVENT + 1

show_text = False
cooked_text = None
cooked_text_rect = None

inventory_open = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            if cook_button_rect.collidepoint(event.pos):
                cook_button_index = 1
            else:
                cook_button_index = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if cook_button_rect.collidepoint(event.pos):
                cook_button_index = 2
                cook_button_clicked = True 
            elif inventory_open and event.button == 1:
                mouse_x, mouse_y = event.pos
                new_position = (mouse_x - inventory.image_rect.x, mouse_y - inventory.image_rect.y)
                inventory.move_item("Egg", new_position)
        elif event.type == pygame.MOUSEBUTTONUP:
            if cook_button_rect.collidepoint(event.pos) and cook_button_clicked:
                cook_button_index = 1
                cooked = cooking.cook(["Bread", "Egg"], "Fried Egg on Toast")
                cooked_text, cooked_text_rect, show_text = cooked
                cook_button_clicked = False
            else:
                cook_button_clicked = False
        elif event.type == HIDE_TEXT_EVENT:
            show_text = False
            pygame.time.set_timer(HIDE_TEXT_EVENT, 0)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                inventory_open = not inventory_open

    screen.fill((0, 0, 0)) 

    if inventory_open:
        inventory.open(screen)
    
    screen.blit(cook_button[cook_button_index], cook_button_rect)
    
    if show_text and cooked_text is not None:
        screen.blit(cooked_text, cooked_text_rect)

    pygame.display.update()
    clock.tick(60)