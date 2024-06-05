import pygame
from sys import exit
from cooking import Cooking

screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

cooking = Cooking(r"Iteration 1\ui\recipes.json")

pygame.init()

cook_button_default = pygame.image.load(r"Iteration 1\assets\ui\cooking\button_cook_defaut.png").convert_alpha()
cook_button_hover = pygame.image.load(r"Iteration 1\assets\ui\cooking\button_cook_hover.png").convert_alpha()
cook_button_clicked = pygame.image.load(r"Iteration 1\assets\ui\cooking\button_cook_clicked.png").convert_alpha()
cook_button = [cook_button_default, cook_button_hover, cook_button_clicked]
cook_button_index = 0
cook_button_rect = cook_button_default.get_rect(center=(screen_width / 2, screen_height / 2)) 

HIDE_TEXT_EVENT = pygame.USEREVENT + 1

def cook(ingredients):
    matching_recipes = cooking.check_recipes(ingredients)
    if matching_recipes:
        recipe_names = matching_recipes
        recipe_text = ", ".join(recipe_names)
        text = f"You just made {recipe_text}!"
    else:
        text = "You cant make anything with that"
    font = pygame.font.Font(None, 36)
    rendered_text = font.render(text, True, (255, 255, 255))
    text_rect = rendered_text.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
    pygame.time.set_timer(HIDE_TEXT_EVENT, 3000)
    return rendered_text, text_rect, True

show_text = False
cooked_text = None
cooked_text_rect = None

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
        elif event.type == pygame.MOUSEBUTTONUP:
            if cook_button_rect.collidepoint(event.pos) and cook_button_clicked:
                cook_button_index = 1
                cooked = cook(["Bread", "Egg"])
                cooked_text, cooked_text_rect, show_text = cooked
                cook_button_clicked = False
            else:
                cook_button_clicked = False
        elif event.type == HIDE_TEXT_EVENT:
            show_text = False
            pygame.time.set_timer(HIDE_TEXT_EVENT, 0)
                    
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(cook_button[cook_button_index], cook_button_rect)
    
    if show_text and cooked_text is not None:
        screen.blit(cooked_text, cooked_text_rect)

    pygame.display.update()
    clock.tick(60)
