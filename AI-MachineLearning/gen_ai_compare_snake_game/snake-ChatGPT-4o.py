import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH = 600
HEIGHT = 400

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Snake settings
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Font settings
FONT_STYLE = pygame.font.SysFont("bahnschrift", 25)
SCORE_FONT = pygame.font.SysFont("comicsansms", 20)

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

def display_score(score):
    value = SCORE_FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH - SNAKE_BLOCK, SNAKE_BLOCK)
    food_y = random.randrange(0, HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message = FONT_STYLE.render("You Lost! Press C to Play Again or Q to Quit", True, RED)
            screen.blit(message, [WIDTH // 6, HEIGHT // 3])
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -SNAKE_BLOCK, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = SNAKE_BLOCK, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, SNAKE_BLOCK

        x += dx
        y += dy
        
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        display_score(snake_length - 1)
        
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - SNAKE_BLOCK, SNAKE_BLOCK)
            food_y = random.randrange(0, HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
