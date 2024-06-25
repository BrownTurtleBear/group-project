import pygame
import math
from sys import exit


class UI:
    def __init__(self, screen, clicked):
        self.screen = screen
        self.x_pos = 50
        self.y_pos = 50
        self.sc_width = 0
        self.sc_height = 0
        self.speed = 2
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
        self.shape_dict = {}
        self.exit = bool
        self.clicked = clicked
        self.settings = True
        self.volume = 50

    def idle(self):
        print(None)

    def move_up_down(self, key_walk):
        self.y_pos += key_walk

    def move_left_right(self, key_walk):
        self.x_pos += key_walk

    def animate(self):
        if self.menu_option != "Gender":
            pygame.draw.rect(self.screen, self.sprite_values[self.menu_option][0],
                             pygame.Rect(self.x_pos, self.y_pos, 20, 20))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y_pos > 10:
                self.move_up_down(-1 * self.speed)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.y_pos < self.sc_height - 10:
                self.move_up_down(1 * self.speed)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x_pos > 10:
                self.move_left_right(-1 * self.speed)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.x_pos < self.sc_width - 10:
                self.move_left_right(1 * self.speed)
        else:
            self.idle()

    def customisation(self, x, y):
        self.sc_width = self.screen.get_width()
        self.sc_height = self.screen.get_height()
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, (3, 7, 252), pygame.Rect(x, y, self.sc_width - (x * 2), self.sc_height - (x * 2)))
        pygame.draw.rect(self.screen, (200, 255, 255),
                         pygame.Rect(x * 2, self.sc_height * 0.5, self.sc_width - (x * 4), self.sc_height * 0.45))
        pygame.draw.rect(self.screen, "Black",
                         pygame.Rect(x * 2, self.sc_height * 0.5, self.sc_width - (x * 4), self.sc_height * 0.45), 3)
        font = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 30)
        text = font.render("Character Customisation", False, "White")
        text_rect = text.get_rect(center=(self.sc_width / 2, 35))
        box_im = pygame.image.load('../assets/ui/menu/box1.png')
        # Section Boxes
        for i, value in enumerate(self.sprite_values.keys()):
            if self.menu_option == value:
                box_im = pygame.transform.scale(box_im, (60, 60))
                box_im_rect = box_im.get_rect(center=((x * 2) + (50 / 2) + (50 * i), 175))
            else:
                box_im = pygame.transform.scale(box_im, (50, 50))
                box_im_rect = box_im.get_rect(center=((x * 2) + (50 / 2) + (50 * i), 175))
            if box_im_rect.collidepoint(pos) and self.menu_option != value:
                box_im = pygame.transform.scale(box_im, (55, 55))
                box_im_rect = box_im.get_rect(center=((x * 2) + (50 / 2) + (50 * i), 175))
                if pygame.mouse.get_pressed()[0] == 1:
                    self.menu_option = value
            self.screen.blit(box_im, box_im_rect)
        # Colour Boxes
        if self.menu_option != "Gender":
            pygame.draw.rect(self.screen, "White", pygame.Rect(x * 3, self.sc_height * 0.58,
                                                               (self.sc_width - (x * 4)) * 0.5,
                                                               self.sc_height / 2.5 - x * 2))
            pygame.draw.rect(self.screen, "Black", pygame.Rect(x * 3, self.sc_height * 0.58,
                                                               (self.sc_width - (x * 4)) * 0.5,
                                                               self.sc_height / 2.5 - x * 2), 3)
            pygame.draw.rect(self.screen, "White",
                             pygame.Rect((self.sc_width - (x * 4) * 0.5) / 2 + 10, self.sc_height * 0.58,
                                         (self.sc_width - (x * 4)) * 0.5 - 10, self.sc_height / 2.5 - x * 2))
            pygame.draw.rect(self.screen, "Black",
                             pygame.Rect((self.sc_width - (x * 4) * 0.5) / 2 + 10, self.sc_height * 0.58,
                                         (self.sc_width - (x * 4)) * 0.5 - 10, self.sc_height / 2.5 - x * 2), 3)
            font1 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 25)
            # Menu Text
            text1 = font1.render(self.menu_option, False, "Black")
            text1_rect = text1.get_rect(center=(self.sc_width / 2, self.sc_height / 2 + 15))
            self.screen.blit(text1, text1_rect)
            font2 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 20)
            text2 = font2.render("Style", False, "Black")
            text2_rect = text2.get_rect(center=((self.sc_width - (x * 4) * 0.5) / 4 + 20, self.sc_height * 0.6 + 10))
            self.screen.blit(text2, text2_rect)
            text3 = font2.render("Colour", False, "Black")
            text3_rect = text3.get_rect(center=((self.sc_width - (x * 4) * 0.6) * 0.75, self.sc_height * 0.6 + 10))
            self.screen.blit(text3, text3_rect)
            for i, value in enumerate(self.colours_dict[self.menu_option]):
                if i - 6 < 0:
                    x_temp = i
                else:
                    x_temp = i - 6
                y_temp = math.floor(i / 6)
                if value == "Black":
                    temp1 = "Grey"
                else:
                    temp1 = "Black"
                colour_button = pygame.draw.rect(self.screen, value,
                                                 pygame.Rect((self.sc_width - (x * 4) * 0.5) / 1.8 + (25 * x_temp),
                                                             self.sc_height * 0.7 + (25 * y_temp), x * 2, y * 2))
                pygame.draw.rect(self.screen, temp1, pygame.Rect((self.sc_width - (x * 4) * 0.5) / 1.8 + (25 * x_temp),
                                                                 self.sc_height * 0.7 + (25 * y_temp), x * 2, y * 2), 1)
                if colour_button.collidepoint(pos):
                    pygame.draw.rect(self.screen, temp1,
                                     pygame.Rect((self.sc_width - (x * 4) * 0.5) / 1.8 + (25 * x_temp),
                                                 self.sc_height * 0.7 + (25 * y_temp), x * 2, y * 2), 2)
                    if pygame.mouse.get_pressed()[0] == 1:
                        self.sprite_values[self.menu_option][0] = value
        else:
            pygame.draw.rect(self.screen, "White", pygame.Rect(x * 3, self.sc_height * 0.58,
                                                               (self.sc_width - (x * 6)), self.sc_height / 2.5 - x * 2))
            pygame.draw.rect(self.screen, "Black", pygame.Rect(x * 3, self.sc_height * 0.58,
                                                               (self.sc_width - (x * 6)), self.sc_height / 2.5 - x * 2),
                             3)
            font1 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 25)
            text1 = font1.render(self.menu_option, False, "Black")
            text1_rect = text1.get_rect(center=(self.sc_width / 2, self.sc_height / 2 + 20))
            self.screen.blit(text1, text1_rect)
            genders = ["Male", "Female", "None"]
            for i, value in enumerate(genders):
                text2 = font1.render("Male", False, "Black")
                text2_rect = text2.get_rect(center=(self.sc_width * 0.2, self.sc_height * 0.7))
                self.screen.blit(text2, text2_rect)
                text3 = font1.render("Female", False, "Black")
                text3_rect = text3.get_rect(center=(self.sc_width * 0.5, self.sc_height * 0.7))
                self.screen.blit(text3, text3_rect)
                text3 = font1.render("None", False, "Black")
                text3_rect = text3.get_rect(center=(self.sc_width * 0.8, self.sc_height * 0.7))
                self.screen.blit(text3, text3_rect)
                # Buttons
                if self.sprite_values["Gender"] == value:
                    pick_button = pygame.draw.rect(self.screen, "Green",
                                                   pygame.Rect(50 + (120 * i), self.sc_height * 0.75,
                                                               self.sc_width / 6,
                                                               self.sc_height / 8 - 10))
                    pygame.draw.rect(self.screen, "Black", pygame.Rect(50 + (120 * i), self.sc_height * 0.75,
                                                                       self.sc_width / 6, self.sc_height / 8 - 10), 3)
                    text4 = font1.render("Pick", False, "Black")
                    text4_rect = text4.get_rect(center=(self.sc_width * 0.2 + (120 * i), self.sc_height * 0.8))
                else:
                    pick_button = pygame.draw.rect(self.screen, "Red",
                                                   pygame.Rect(50 + (120 * i), self.sc_height * 0.75,
                                                               self.sc_width / 6, self.sc_height / 8 - 10))
                    pygame.draw.rect(self.screen, "Black", pygame.Rect(50 + (120 * i), self.sc_height * 0.75,
                                                                       self.sc_width / 6, self.sc_height / 8 - 10), 3)
                    text4 = font1.render("Pick", False, "Black")
                    text4_rect = text4.get_rect(center=(self.sc_width * 0.2 + (120 * i), self.sc_height * 0.8))
                if pick_button.collidepoint(pos):
                    pick_button = pygame.draw.rect(self.screen, "Green",
                                                   pygame.Rect(50 + (120 * i), self.sc_height * 0.75,
                                                               self.sc_width / 6, self.sc_height / 8 - 10))
                    pygame.draw.rect(self.screen, "Black", pygame.Rect(50 + (120 * i), self.sc_height * 0.75,
                                                                       self.sc_width / 6, self.sc_height / 8 - 10), 3)
                    text4 = font1.render("Pick", False, "Black")
                    text4_rect = text4.get_rect(center=(self.sc_width * 0.2 + (120 * i), self.sc_height * 0.8))
                    if pygame.mouse.get_pressed()[0] == 1:
                        self.sprite_values["Gender"] = value
                self.screen.blit(text4, text4_rect)
        exit_button = pygame.draw.rect(self.screen, "Red", pygame.Rect(self.sc_width * 0.8, 60, 60, 30))
        if exit_button.collidepoint(pos):
            pygame.draw.rect(self.screen, "Black", pygame.Rect(self.sc_width * 0.8, 60, 60, 30), 3)
            if pygame.mouse.get_pressed()[0] == 1:
                self.exit = True
        print(self.exit)
        font2 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 15)
        text2 = font2.render("Exit", False, "Black")
        text2_rect = text2.get_rect(center=(self.sc_width * 0.8 + 30, 75))
        self.screen.blit(text2, text2_rect)
        # Main Menu Text
        self.screen.blit(text, text_rect)
        self.animate()

    def main_menu(self):
        self.sc_width = self.screen.get_width()
        self.sc_height = self.screen.get_height()
        pos = pygame.mouse.get_pos()
        font1 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 50)
        text1 = font1.render("Fishing Sim", False, "Black")
        text1_rect = text1.get_rect(center=(self.sc_width / 2, 60))
        self.screen.blit(text1, text1_rect)
        exit_button = pygame.draw.rect(self.screen, "Red", pygame.Rect(self.sc_width - 70, 10, 60, 30))
        font2 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 15)
        text2 = font2.render("Exit", False, "Black")
        text2_rect = text2.get_rect(center=(self.sc_width - 39, 24))
        self.screen.blit(text2, text2_rect)

        start_button = pygame.draw.rect(self.screen, "Green",
                                        pygame.Rect(self.sc_width / 2 - 80, self.sc_height / 2 - 90, 170, 80))
        font3 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 35)
        text3 = font3.render("Start", False, "Black")
        text3_rect = text3.get_rect(center=(self.sc_width / 2 + 5, self.sc_height / 2 - 50))
        self.screen.blit(text3, text3_rect)

        character_button = pygame.draw.rect(self.screen, "Blue",
                                            pygame.Rect(self.sc_width / 2 - 80, self.sc_height / 2, 170, 80))
        font3 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 35)
        text3 = font3.render("Character", False, "White")
        text3_rect = text3.get_rect(center=(self.sc_width / 2 + 5, self.sc_height / 2 + 40))
        self.screen.blit(text3, text3_rect)

        settings_button = pygame.draw.rect(self.screen, "Grey",
                                           pygame.Rect(self.sc_width / 2 - 80, self.sc_height / 2 + 90, 170, 80))
        font3 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 35)
        text3 = font3.render("Settings", False, "Black")
        text3_rect = text3.get_rect(center=(self.sc_width / 2 + 5, self.sc_height / 2 + 130))
        self.screen.blit(text3, text3_rect)
        if exit_button.collidepoint(pos):
            pygame.draw.rect(self.screen, "Black", pygame.Rect(self.sc_width - 70, 10, 60, 30), 3)
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked[1] = True
            elif self.clicked[1]:
                self.clicked[1] = False
                pygame.quit()
        elif start_button.collidepoint(pos):
            pygame.draw.rect(self.screen, "Black", pygame.Rect(self.sc_width / 2 - 80, self.sc_height / 2 - 90, 170, 80), 5)
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked[1] = True
            elif self.clicked[1]:
                self.clicked[1] = False
                return "start"
        elif character_button.collidepoint(pos):
            pygame.draw.rect(self.screen, "Black", pygame.Rect(self.sc_width / 2 - 80, self.sc_height / 2, 170, 80), 5)
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked[1] = True
            elif self.clicked[1]:
                self.clicked[1] = False
                return "character"
        elif settings_button.collidepoint(pos):
            pygame.draw.rect(self.screen, "Black", pygame.Rect(self.sc_width / 2 - 80, self.sc_height / 2 + 90, 170, 80), 5)
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked[1] = True
            elif self.clicked[1]:
                self.clicked[1] = False
                return "settings"
        return self.clicked

    def settings_menu(self, x, y):
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, "Grey", pygame.Rect(x, y, self.sc_width - (x * 2), self.sc_height - (x * 2)))
        font1 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 50)
        text1 = font1.render("Settings Menu", False, "Black")
        text1_rect = text1.get_rect(center=(self.sc_width / 2, 60))
        self.screen.blit(text1, text1_rect)
        pygame.draw.rect(self.screen, "White",
                         pygame.Rect(self.sc_width / 6, self.sc_height / 4, self.sc_width / 3, self.sc_height / 2))
        font1 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 25)
        text1 = font1.render("Volume", False, "Black")
        text1_rect = text1.get_rect(center=(self.sc_width / 3, self.sc_height / 3 - 10))
        self.screen.blit(text1, text1_rect)
        text1 = font1.render(str(self.volume), False, "Black")
        text1_rect = text1.get_rect(center=(self.sc_width / 4 + 35, self.sc_height / 2 + 10))
        self.screen.blit(text1, text1_rect)

        volume_im = pygame.image.load('../assets/ui/menu/volume.png')
        volume_im = pygame.transform.scale(volume_im, (50, 45))
        volume_im_rect = volume_im.get_rect(center=(90, 210))
        self.screen.blit(volume_im, volume_im_rect)
        up_key = pygame.image.load('../assets/ui/menu/arrow.png')
        up_key = pygame.transform.scale(up_key, (45, 45))
        up_key_rect = up_key.get_rect(center=(135, 160))
        down_key = pygame.transform.flip(up_key, False, True)
        down_key_rect = down_key.get_rect(center=(135, 260))
        self.screen.blit(up_key, up_key_rect)
        self.screen.blit(down_key, down_key_rect)

        exit_button = pygame.draw.rect(self.screen, "Red", pygame.Rect(self.sc_width - 70, 10, 60, 30))
        font2 = pygame.font.Font("text/aller-font/Aller_Bd.ttf", 15)
        text2 = font2.render("Exit", False, "Black")
        text2_rect = text2.get_rect(center=(self.sc_width - 39, 24))
        self.screen.blit(text2, text2_rect)
        if up_key_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.volume < 100:
                    self.volume += 1
        if down_key_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.volume > 0:
                    self.volume -= 1
        if exit_button.collidepoint(pos):
            pygame.draw.rect(self.screen, "Black", pygame.Rect(self.sc_width - 70, 10, 60, 30), 3)
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked[1] = True
            elif self.clicked[1]:
                self.clicked[1] = False
                self.settings = False
                return 'menu'
        else:
            self.settings = True
        return self.clicked, self.settings

    def img_button(self, x, y, w, h, location):
        button = pygame.image.load(location).convert_alpha()
        button = pygame.transform.scale(button, (w, h))
        button_rect = button.get_rect(center=(x, y))
        self.screen.blit(button, button_rect)

    def text(self, x, y, size, colour, text):
        font = pygame.font.Font("../assets/text/aller-font/Aller_Bd.ttf", size)
        text = font.render(text, False, colour)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)

    def button(self, x, y, width, height, colour, type):
        pos = pygame.mouse.get_pos()
        button = pygame.draw.rect(self.screen, colour, pygame.Rect(x, y, width, height))
        if button.collidepoint(pos):
            pygame.draw.rect(self.screen, "Black", pygame.Rect(x, y, width, height), 5)
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked[1] = True
            elif self.clicked[1]:
                self.clicked[1] = False
                self.clicked[0] = type
        return button
