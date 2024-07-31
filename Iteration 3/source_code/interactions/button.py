import pygame


class Button:
    def __init__(self, screen, parent, group, point, x_pos, y_pos, x_scale, y_scale):
        self.screen = screen
        self.pos = {point: (x_pos, y_pos)}
        self.clicked = False
        self.pressed = False
        default = pygame.image.load(f"../assets/sprites/ui/{parent}/button_{group}_default.png").convert_alpha()
        hover = pygame.image.load(f"../assets/sprites/ui/{parent}/button_{group}_hover.png").convert_alpha()
        clicked = pygame.image.load(f"../assets/sprites/ui/{parent}/button_{group}_clicked.png").convert_alpha()
        self.default_image = pygame.transform.scale(default, (
            int(default.get_width() * x_scale), int(default.get_height() * y_scale)))
        self.hover_image = pygame.transform.scale(hover,
                                                  (int(hover.get_width() * x_scale), int(hover.get_height() * y_scale)))
        self.clicked_image = pygame.transform.scale(clicked, (
            int(clicked.get_width() * x_scale), int(clicked.get_height() * y_scale)))

        self.rect = self.default_image.get_rect(topleft=self.pos[point])

        self.group = group

    def update(self, mouse_tracker):
        mouse_pos = pygame.mouse.get_pos()
        self.clicked = False

        if self.rect.collidepoint(mouse_pos):
            if mouse_tracker.get_just_pressed():
                self.pressed = True
            elif mouse_tracker.get_just_released():
                if self.pressed:
                    self.clicked = True
                self.pressed = False
            else:
                self.pressed = mouse_tracker.get_pressed()
        else:
            if mouse_tracker.get_just_released():
                self.pressed = False
            elif not mouse_tracker.get_pressed():
                self.pressed = False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.pressed:
            self.screen.blit(self.clicked_image, self.pos[list(self.pos.keys())[0]])
        elif self.rect.collidepoint(mouse_pos):
            self.screen.blit(self.hover_image, self.pos[list(self.pos.keys())[0]])
        else:
            self.screen.blit(self.default_image, self.pos[list(self.pos.keys())[0]])
