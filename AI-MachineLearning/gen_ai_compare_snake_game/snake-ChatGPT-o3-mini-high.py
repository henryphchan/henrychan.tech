import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Game settings
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
CELL_SIZE = 20

# Make sure the window dimensions are multiples of the cell size
assert WINDOW_WIDTH % CELL_SIZE == 0, "Window width must be a multiple of cell size."
assert WINDOW_HEIGHT % CELL_SIZE == 0, "Window height must be a multiple of cell size."
CELL_WIDTH = WINDOW_WIDTH // CELL_SIZE
CELL_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the clock for a decent framerate
fps_clock = pygame.time.Clock()
FPS = 10  # Adjust this to make the snake move faster or slower

# Define colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)

def get_random_location():
    """Return a random location on the grid."""
    x = random.randint(0, CELL_WIDTH - 1) * CELL_SIZE
    y = random.randint(0, CELL_HEIGHT - 1) * CELL_SIZE
    return [x, y]

def game_over(score):
    """Display Game Over screen and exit."""
    font = pygame.font.SysFont('arial', 36)
    text_surface = font.render(f'Game Over! Score: {score}', True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    window.blit(text_surface, text_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

def main():
    # Initial snake: a list of [x, y] positions (head is the first element)
    snake = [[100, 100], [80, 100], [60, 100]]
    direction = "RIGHT"
    change_to = direction

    # Place the first apple
    apple = get_random_location()
    score = 0

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check for key presses
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

        # Update the snake direction
        direction = change_to

        # Calculate new head position based on the direction
        head = snake[0].copy()
        if direction == "UP":
            head[1] -= CELL_SIZE
        elif direction == "DOWN":
            head[1] += CELL_SIZE
        elif direction == "LEFT":
            head[0] -= CELL_SIZE
        elif direction == "RIGHT":
            head[0] += CELL_SIZE

        # Insert new head into the snake's body
        snake.insert(0, head)

        # Check if snake has eaten the apple
        if head == apple:
            score += 1
            apple = get_random_location()
        else:
            # Remove the tail segment if no apple is eaten
            snake.pop()

        # Check for collisions with the boundaries
        if (head[0] < 0 or head[0] >= WINDOW_WIDTH or
            head[1] < 0 or head[1] >= WINDOW_HEIGHT):
            game_over(score)

        # Check for collisions with itself
        if head in snake[1:]:
            game_over(score)

        # Draw everything
        window.fill(BLACK)  # Clear the screen with black

        # Draw the apple
        pygame.draw.rect(window, RED, pygame.Rect(apple[0], apple[1], CELL_SIZE, CELL_SIZE))

        # Draw the snake segments
        for segment in snake:
            pygame.draw.rect(window, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        # Update the display
        pygame.display.flip()

        # Control the game speed
        fps_clock.tick(FPS)

if __name__ == "__main__":
    main()
