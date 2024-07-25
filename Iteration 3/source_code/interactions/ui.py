import pygame
from controls.mouse_tracker import MouseTracker


class UI:
    def __init__(self, screen):
        self.screen = screen
        self.mouse_tracker = MouseTracker()
        self.clicked = False
        self.menu_option = "Gender"
        self.sprite_values = {}
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

    def image_button(self, x, y, button):
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
