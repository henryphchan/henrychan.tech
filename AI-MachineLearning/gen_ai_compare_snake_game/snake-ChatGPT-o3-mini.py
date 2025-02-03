import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red   = (213, 50, 80)
green = (0, 255, 0)
blue  = (50, 153, 213)

# Define game settings
snake_block = 10
snake_speed = 15  # Increase this value to make the game faster

clock = pygame.time.Clock()

# Set up fonts for messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Display a message on the screen."""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def gameLoop():
    """Main game loop."""
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # Initial movement
    x1_change = 0
    y1_change = 0

    # Snake data: list of segments; starting with one segment
    snake_List = []
    Length_of_snake = 1

    # Place the first food item
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        # Game Over screen loop
        while game_close:
            screen.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  # Restart the game
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Movement events
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

        # Check for boundaries collision
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)

        # Draw the food
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        
        # Update snake segments
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for collision with itself
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        # Check if snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Control the speed of the snake
        clock.tick(snake_speed)

    pygame.quit()

if __name__ == "__main__":
    gameLoop()
