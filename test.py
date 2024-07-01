import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake properties
snake_block = 20
snake_speed = 15

# Font
font = pygame.font.SysFont(None, 30)

# Initialize snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

# Display score
def display_score(score):
    value = font.render("Score: " + str(score), True, WHITE)
    window.blit(value, [10, 10])

# Display number of apples
def display_apple_count(count):
    value = font.render("Apples: " + str(count), True, WHITE)
    window.blit(value, [10, 40])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Apple properties
    apple_count = 3
    apples = []

    clock = pygame.time.Clock()

    # Generate initial apples
    for _ in range(apple_count):
        foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
        foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
        apples.append([foodx, foody])

    while not game_over:
        while game_close:
            window.fill(BLACK)
            message = font.render("You Lost! Press Q-Quit or C-Play Again", True, WHITE)
            window.blit(message, [width / 6, height / 3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    apple_count += 1
                    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
                    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
                    apples.append([foodx, foody])
                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    if apple_count > 1:
                        apple_count -= 1
                        apples.pop()

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)

        for apple in apples:
            pygame.draw.rect(window, RED, [apple[0], apple[1], snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)
        display_apple_count(apple_count)

        pygame.display.update()

        for apple in apples:
            if x1 == apple[0] and y1 == apple[1]:
                foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
                foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
                apples[apples.index(apple)] = [foodx, foody]
                length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

gameLoop()