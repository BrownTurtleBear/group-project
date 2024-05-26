import pygame
import urllib.request
import io
from sys import exit

# General setup
pygame.init( )

# Game Screen
screen_width = 800
screen_height= 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gaym')

# For Frame rate
clock = pygame.time.Clock()

# font
font_url = "https://raw.githubusercontent.com/BrownTurtleBear/group-project/blob/main/Tommo/tutorial/assets/font/Pixeltype.ttf"
font = pygame.font.Font(None, 50)

# box
# test_surface = pygame.Surface((screen_width, 100))
# test_surface.fill('Yellow')

# images
sky_url = "https://raw.githubusercontent.com/BrownTurtleBear/group-project/main/Tommo/tutorial/assets/graphics/Sky.png"
with urllib.request.urlopen(sky_url) as url_response:
    sky_surface = pygame.image.load(io.BytesIO(url_response.read()))

ground_url = "https://raw.githubusercontent.com/BrownTurtleBear/group-project/main/Tommo/tutorial/assets/graphics/ground.png"
with urllib.request.urlopen(ground_url) as url_response:
    ground_surface = pygame.image.load(io.BytesIO(url_response.read()))

# text
text_surface = font.render("Yoooour GAYYY", False, "Green")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # drawing elements
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    # update everything
    pygame.display.update()
    clock.tick(60) # 60 fps