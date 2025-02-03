import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# -----------------------------
# Game Configuration
# -----------------------------
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
CELL_SIZE = 20   # Size of a grid cell

# Derived game parameters
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (40, 40, 40)

# Frames per second (speed of the game)
FPS = 10

# Direction vectors for snake movement
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# -----------------------------
# Helper Functions
# -----------------------------
def draw_cell(surface, color, x, y):
    """Draw a single cell (rectangle) on the surface."""
    pygame.draw.rect(
        surface,
        color,
        (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )

def random_food_position():
    """Generate a random (x, y) position for new food."""
    return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

def game_over_screen(surface, score):
    """Display the game over screen and final score."""
    font = pygame.font.SysFont("Arial", 32, bold=True)
    text = font.render(f"Game Over! Score: {score}", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    
    surface.fill(BLACK)
    surface.blit(text, text_rect)
    pygame.display.flip()
    
    # Wait for a few seconds or until user closes window
    pygame.time.wait(3000)

# -----------------------------
# Main Game Function
# -----------------------------
def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Snake Game")

    # Initial snake settings
    snake_positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]  # Starting in center
    snake_direction = RIGHT  # Start moving to the right
    snake_length = 3         # Initial length
    
    # Place the first food
    food_position = random_food_position()

    score = 0
    running = True

    while running:
        clock.tick(FPS)

        # -----------------------------
        # Handle events (keyboard, etc.)
        # -----------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT

        # -----------------------------
        # Update snake position
        # -----------------------------
        head_x, head_y = snake_positions[0]
        move_x, move_y = snake_direction
        new_head = (head_x + move_x, head_y + move_y)

        # Check for collisions with walls (wrap around)
        # If you want the game to end on wall collision instead of wrapping, comment these lines:
        new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)

        # Insert new head at the beginning of the list
        snake_positions.insert(0, new_head)

        # Check if snake eats food
        if new_head == food_position:
            score += 1
            snake_length += 1
            food_position = random_food_position()
        else:
            # Remove the tail if no food is eaten
            snake_positions.pop()

        # Check for collisions with itself (excluding the very tail since we might have just removed it)
        if new_head in snake_positions[1:]:
            # Game over
            game_over_screen(screen, score)
            running = False
            continue  # to exit the loop

        # -----------------------------
        # Draw everything
        # -----------------------------
        screen.fill(BLACK)

        # Draw snake
        for x, y in snake_positions:
            draw_cell(screen, GREEN, x, y)

        # Draw food
        fx, fy = food_position
        draw_cell(screen, RED, fx, fy)

        # (Optional) Draw grid for visual effect
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))

        # Update the display
        pygame.display.update()

    # After the loop ends, we can quit the game
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
