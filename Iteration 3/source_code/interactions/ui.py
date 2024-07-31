import pygame
from controls.mouse_tracker import MouseTracker


class UI:
    def __init__(self, screen):
        self.screen = screen
        self.mouse_tracker = MouseTracker()
        self.clicked = False
        self.menu_option = "Gender"
        self.sprite_values = {
            "Gender": "None",
            "Hair": ["White", 0],
            "Eyes": ["Black", 0],
            "Clothing 1": ["Black", 0],
            "Clothing 2": ["Black", 0],
            "Hat": ["Black", 0],
            "Body": ["Brown", 0]}
        self.colours_dict = {
            "Hair": ["White", "Black", "Yellow", "Red", "Blue", "Brown"],
            "Eyes": ["Black", "Brown", "Green", "Blue", "Crimson"],
            "Clothing 1": ["Black", "Brown", "Green", "Blue", "Red", "White", "Orange"],
            "Clothing 2": ["Black", "Brown", "Green", "Blue", "Red", "White", "Orange"],
            "Hat": ["Black", "Brown", "Green", "Blue", "Red", "White", "Orange", "Grey"],
            "Body": ["Brown"]
        }
        self.style_dict = {}

        # Button cook
        # Load
        button_cook_default = pygame.image.load("../assets/sprites/ui/cooking/button_cook_default.png").convert_alpha()
        button_cook_hover = pygame.image.load("../assets/sprites/ui/cooking/button_cook_hover.png").convert_alpha()
        button_cook_clicked = pygame.image.load("../assets/sprites/ui/cooking/button_cook_clicked.png").convert_alpha()
        # Scale
        button_cook_default_scaled = pygame.transform.scale(button_cook_default, (
            button_cook_default.get_width() * 0.9, button_cook_default.get_height() * 0.9))
        button_cook_hover_scaled = pygame.transform.scale(button_cook_hover, (
            button_cook_hover.get_width() * 0.9, button_cook_hover.get_height() * 0.9))
        button_cook_clicked_scaled = pygame.transform.scale(button_cook_clicked, (
            button_cook_clicked.get_width() * 0.9, button_cook_clicked.get_height() * 0.9))

        # Button next
        button_next_default = pygame.image.load("../assets/sprites/ui/cooking/button_next_default.png").convert_alpha()
        button_next_hover = pygame.image.load("../assets/sprites/ui/cooking/button_next_hover.png").convert_alpha()
        button_next_clicked = pygame.image.load("../assets/sprites/ui/cooking/button_next_clicked.png").convert_alpha()
        # Scale
        button_next_default_scaled = pygame.transform.scale(button_next_default, (
            button_next_default.get_width() * 0.6, button_next_default.get_height() * 0.6))
        button_next_hover_scaled = pygame.transform.scale(button_next_hover, (
            button_next_hover.get_width() * 0.6, button_next_hover.get_height() * 0.6))
        button_next_clicked_scaled = pygame.transform.scale(button_next_clicked, (
            button_next_clicked.get_width() * 0.6, button_next_clicked.get_height() * 0.6))

        # Assign scaled images to the dictionary
        self.img_buttons = {
            "cook": {
                "default": button_cook_default_scaled,
                "hover": button_cook_hover_scaled,
                "clicked": button_cook_clicked_scaled,
            },
            "next": {
                "default": button_next_default_scaled,
                "hover": button_next_hover_scaled,
                "clicked": button_next_clicked_scaled,
            }
        }

    def outlined_rect(self, x, y, w, h, outline, colour):
        pygame.draw.rect(self.screen, colour, pygame.Rect((x, y), (w, h)))
        pygame.draw.rect(self.screen, "Black", pygame.Rect((x, y), (w, h)), outline)

    def image(self, x, y, w, h, location):
        image = pygame.image.load(location)
        image = pygame.transform.scale(image, (w, h))
        image_rect = image.get_rect(center=(x, y))
        self.screen.blit(image, image_rect)

    def text(self, x, y, size, colour, text):
        font = pygame.font.Font("../assets/fonts/aller-font/Aller_Bd.ttf", size)
        text = font.render(text, False, colour)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)

    def button(self, type, hold, x, y, width, height, colour, location):
        pos = pygame.mouse.get_pos()
        if type == "rect":
            button_rect = pygame.draw.rect(self.screen, colour, pygame.Rect(x, y, width, height))
            pygame.draw.rect(self.screen, "Black", pygame.Rect(x, y, width, height), 1)
        elif type == "img":
            button = pygame.image.load(location).convert_alpha()
            button = pygame.transform.scale(button, (width, height))
            button_rect = button.get_rect(center=(x, y))
            self.screen.blit(button, button_rect)
        else:
            button, button_rect = None, None
        if button_rect.collidepoint(pos):
            if type == "rect":
                pygame.draw.rect(self.screen, "Black", pygame.Rect(x, y, width, height), 3)
            elif type == "img":
                button = pygame.transform.scale(button, (width, height))
                button_rect = button.get_rect(center=(x, y))
                self.screen.blit(button, button_rect)
            if not hold:
                if pygame.mouse.get_pressed()[0] == 1:
                    self.clicked = True
                elif self.clicked:
                    self.clicked = False
                    return True
            else:
                if pygame.mouse.get_pressed()[0] == 1:
                    return True

    def better_image_button(self, button, point, x_pos, y_pos):
        mouse_pos = pygame.mouse.get_pos()
        self.mouse_tracker.update_mouse_states()
        mouse_released = self.mouse_tracker.get_just_released()[0]
        mouse_clicking = pygame.mouse.get_pressed()[0]
        p = {point: (x_pos, y_pos)}
        rect = self.img_buttons[button]["default"].get_rect(**p)
        if rect.collidepoint(mouse_pos) and (mouse_clicking or mouse_released):
            if mouse_released:
                clicked = True
            else:
                clicked = False
            status = "clicked"
        elif rect.collidepoint(mouse_pos) and not mouse_clicking:
            status = "hover"
            clicked = False
        else:
            status = "default"
            clicked = False
        self.screen.blit(self.img_buttons[button][status], rect)
        return clicked

    def better_text(self, point, x_pos, y_pos, size, colour, text):
        font = pygame.font.Font("../assets/fonts/aller-font/Aller_Bd.ttf", size)
        text = font.render(text, False, colour)
        p = {point: (x_pos, y_pos)}
        text_rect = text.get_rect(**p)
        self.screen.blit(text, text_rect)
