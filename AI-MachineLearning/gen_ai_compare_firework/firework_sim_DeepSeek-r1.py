import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.2
FPS = 30

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Firework Display")
clock = pygame.time.Clock()

class Firework:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = SCREEN_HEIGHT  # Start at the bottom
        self.target_y = random.randint(SCREEN_HEIGHT // 4, SCREEN_HEIGHT // 2)
        self.velocity = -random.randint(5, 10)  # Move upwards
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.exploded = False

    def explode(self, particles):
        # Create multiple particles
        for _ in range(100):
            particles.append(Particle(self.x, self.y, self.color))
        self.exploded = True

    def update(self, particles):
        if not self.exploded:
            self.y += self.velocity
            if self.y <= self.target_y:
                self.explode(particles)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 5)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.color = color
        self.timer = 255  # Fade-out timer
        self.radius = 3

    def update(self):
        self.vy += GRAVITY
        self.x += self.vx
        self.y += self.vy
        self.timer -= 5  # Decrease alpha (fade out)
        self.radius = max(0, int(self.timer / 255 * 3))

    def is_alive(self):
        return self.timer > 0

def main():
    running = True
    fireworks = []
    particles = []
    last_launch_time = pygame.time.get_ticks()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Launch new fireworks periodically
        current_time = pygame.time.get_ticks()
        if current_time - last_launch_time > 1500:  # 1.5 seconds
            fireworks.append(Firework())
            last_launch_time = current_time

        # Update fireworks
        for firework in fireworks[:]:
            firework.update(particles)
            if firework.exploded:
                fireworks.remove(firework)

        # Update particles
        for particle in particles[:]:
            particle.update()
            if not particle.is_alive():
                particles.remove(particle)

        # Draw everything
        screen.fill((0, 0, 0))  # Black background

        # Draw fireworks (pre-explosion)
        for firework in fireworks:
            if not firework.exploded:
                pygame.draw.circle(screen, firework.color, (int(firework.x), int(firework.y)), 3)

        # Draw particles
        for particle in particles:
            # Calculate faded color
            faded_color = (
                particle.color[0] * particle.timer // 255,
                particle.color[1] * particle.timer // 255,
                particle.color[2] * particle.timer // 255
            )
            pygame.draw.circle(screen, faded_color, (int(particle.x), int(particle.y)), particle.radius)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()