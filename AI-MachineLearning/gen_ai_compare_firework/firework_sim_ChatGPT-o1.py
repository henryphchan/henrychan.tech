import turtle
import random
import time

def draw_firework(t, x, y, size=100, rays=20):
    """
    Draws a single firework at coordinates (x, y) with
    `rays` lines (or sparks) and a 'size' length.
    """
    # Move turtle to the start position
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Choose a random color
    t.color(random.random(), random.random(), random.random())

    # Draw the explosion
    for _ in range(rays):
        t.forward(size)
        t.backward(size)
        t.left(360 / rays)

def main():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Fireworks Demo")

    # Create a turtle
    t = turtle.Turtle()
    t.speed(0)          # Fastest speed
    t.hideturtle()      # Hide the turtle cursor

    # Number of fireworks you want to launch
    fireworks_count = 7

    # Draw multiple fireworks in random positions
    for _ in range(fireworks_count):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        size = random.randint(50, 150)
        rays = random.randint(12, 30)
        
        draw_firework(t, x, y, size=size, rays=rays)
        
        # Pause so you can see the firework before clearing
        time.sleep(1.0)
        
        # Clear only the firework lines—keep screen background
        t.clear()

    # Optional: Keep the window open until clicked
    screen.exitonclick()

if __name__ == "__main__":
    main()
