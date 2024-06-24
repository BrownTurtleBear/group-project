from ui import UI
import pygame
ui = UI()
menu = "main"
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


while True:
    screen.fill('black')
    if menu == "main":
        pos = pygame.mouse.get_pos()
        text, text_rect = ui.text(screen.get_width()/2, 60, 50)
        screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    clock.tick(60)