import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Game settings
clock = pygame.time.Clock()
block_size = 20
game_speed = 15

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Initialize snake
snake = [(window_width//2, window_height//2)]
snake_direction = 'RIGHT'
score = 0

# Generate initial food position
def generate_food():
    while True:
        x = random.randint(0, (window_width - block_size) // block_size) * block_size
        y = random.randint(0, (window_height - block_size) // block_size) * block_size
        if (x, y) not in snake:
            return (x, y)

food = generate_food()

# Font for score display
font = pygame.font.SysFont(None, 55)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    # Move the snake
    head_x, head_y = snake[0]
    if snake_direction == 'UP':
        new_head = (head_x, head_y - block_size)
    elif snake_direction == 'DOWN':
        new_head = (head_x, head_y + block_size)
    elif snake_direction == 'LEFT':
        new_head = (head_x - block_size, head_y)
    elif snake_direction == 'RIGHT':
        new_head = (head_x + block_size, head_y)

    # Check for collisions
    if (new_head[0] < 0 or new_head[0] >= window_width or 
        new_head[1] < 0 or new_head[1] >= window_height or 
        new_head in snake):
        # Game Over
        screen.fill(black)
        game_over_text = font.render(f'Game Over! Score: {score}', True, red)
        screen.blit(game_over_text, (window_width//2 - 180, window_height//2 - 20))
        pygame.display.update()
        pygame.time.wait(2000)
        running = False
        continue

    snake.insert(0, new_head)

    # Check if food is eaten
    if new_head == food:
        score += 1
        food = generate_food()
    else:
        snake.pop()

    # Draw everything
    screen.fill(black)
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], block_size, block_size))
    pygame.draw.rect(screen, red, (food[0], food[1], block_size, block_size))
    
    # Display score
    score_text = font.render(f'Score: {score}', True, green)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(game_speed)

pygame.quit()