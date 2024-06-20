import pygame
import pygame_gui

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame GUI Custom Image Button')

manager = pygame_gui.UIManager((800, 600), theme_path="quick_start.json")

button_images = {
    "normal": pygame.image.load("Iteration 1/assets/ui/cooking/button_cook_default.png"),
    "hovered": pygame.image.load("Iteration 1/assets/ui/cooking/button_cook_hovered.png"),
    "selected": pygame.image.load("Iteration 1/assets/ui/cooking/button_cook_clicked.png")
}

button_rect = pygame.Rect((100, 100), (200, 50))
button = pygame_gui.elements.UIButton(
    relative_rect=button_rect,
    text='',
    manager=manager,
    normal_bg_image_surface=button_images["normal"],
    hovered_bg_image_surface=button_images["hovered"],
    selected_bg_image_surface=button_images["selected"]
)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    screen.fill((255, 255, 255))

    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
