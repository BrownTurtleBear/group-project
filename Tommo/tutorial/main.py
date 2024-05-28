import pygame
from sys import exit

# General setup
pygame.init()

# Game Screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gaym')

# For Frame rate
clock = pygame.time.Clock()

# font
font = pygame.font.Font(r"assets/font/Pixeltype.ttf", 50)

# text
text_surface = font.render("Your GAY", False, (64, 64, 64))
text_rectangle = text_surface.get_rect(center=(screen_width / 2, 50))

# box
# test_surface = pygame.Surface((screen_width, 100))
# test_surface.fill('Yellow')

# images
sky_surface = pygame.image.load(r"assets\graphics\Sky.png").convert()
ground_surface = pygame.image.load(r"assets\graphics\ground.png").convert()

# moving image
snail_surface = pygame.image.load(r"assets\graphics\snail\snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(0, 300))

# using rectangles
player_surface = pygame.image.load(r"assets\graphics\Player\player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rectangle.collidepoint(event.pos):
                print("stop touching me uwu")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("☄️☄️☄️☄️")

    # drawing elements
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", text_rectangle)
    pygame.draw.rect(screen, "#c0e8ec", text_rectangle, 10)
    screen.blit(text_surface, text_rectangle)
    snail_rectangle.left -= 4
    if snail_rectangle.left < 0:
        snail_rectangle.left = screen_width
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("Space 🚀")

    # pygame.draw.line(screen, "Yellow", (0, 0), pygame.mouse.get_pos(), 20)
    # pygame.draw.ellipse(screen, "Green", pygame.Rect(50, 200, 100, 100))

    # collision
    if player_rectangle.colliderect(snail_rectangle):
        print('collision')

    # update everything
    pygame.display.update()
    clock.tick(60)  # 60 fps
