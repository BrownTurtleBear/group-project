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

        self.img_buttons = {
            "cook": {
                "default": pygame.transform.scale(pygame.image.load(
                    "../assets/sprites/ui/cooking/button_cook_default.png").convert_alpha(), (
                                                      pygame.image.load(
                                                          "../assets/sprites/ui/cooking/button_cook_default.png").convert_alpha().get_width() * 0.9,
                                                      pygame.image.load(
                                                          "../assets/sprites/ui/cooking/button_cook_default.png").convert_alpha().get_height() * 0.9)),
                "hover": pygame.transform.scale(pygame.image.load(
                    "../assets/sprites/ui/cooking/button_cook_hover.png").convert_alpha(), (
                                                    pygame.image.load(
                                                        "../assets/sprites/ui/cooking/button_cook_hover.png").convert_alpha().get_width() * 0.9,
                                                    pygame.image.load(
                                                        "../assets/sprites/ui/cooking/button_cook_hover.png").convert_alpha().get_height() * 0.9)),
                "clicked": pygame.transform.scale(pygame.image.load(
                    "../assets/sprites/ui/cooking/button_cook_clicked.png").convert_alpha(), (
                                                      pygame.image.load(
                                                          "../assets/sprites/ui/cooking/button_cook_clicked.png").convert_alpha().get_width() * 0.9,
                                                      pygame.image.load(
                                                          "../assets/sprites/ui/cooking/button_cook_clicked.png").convert_alpha().get_height() * 0.9)),
            }
        }

    def outlined_rect(self, x, y, w, h, outline, colour):
        pygame.draw.rect(self.screen, colour, pygame.Rect((x, y), (w, h)))
        pygame.draw.rect(self.screen, "Black", pygame.Rect((x, y), (w, h)), outline)

    def text(self, x, y, size, colour, text):
        font = pygame.font.Font("../assets/fonts/aller-font/Aller_Bd.ttf", size)
        text = font.render(text, False, colour)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)

    def image(self, x, y, w, h, location):
        button = pygame.image.load(location).convert_alpha()
        button = pygame.transform.scale(button, (w, h))
        button_rect = button.get_rect(center=(x, y))
        self.screen.blit(button, button_rect)

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

    def image_button(self, x, y, button):
        pos = pygame.mouse.get_pos()
        button_rect = button[0].get_rect(center=(x, y))
        self.screen.blit(button[0], button_rect)
        if button_rect.collidepoint(pos):
            button_rect = button[1].get_rect(center=(x, y))
            self.screen.blit(button, button_rect)
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
            elif self.clicked:
                self.clicked = False
                button_rect = button[2].get_rect(center=(x, y))
                self.screen.blit(button, button_rect)
                return True

    def better_image_button(self, button, point, x_pos, y_pos):
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = self.mouse_tracker.get_just_pressed()[0]
        p = {point: (x_pos, y_pos)}
        rect = self.img_buttons[button]["default"].get_rect(**p)
        if not rect.collidepoint(mouse_pos):
            status = "default"
            clicked = False
        else:
            if mouse_clicked:
                print("penis")
                status = "clicked"
                clicked = True
            else:
                status = "hover"
                clicked = False
        self.screen.blit(self.img_buttons[button][status], rect)
        return clicked

