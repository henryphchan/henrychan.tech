import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireworks Simulation")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Global constants
GRAVITY = 0.1  # acceleration due to gravity
PARTICLE_COUNT = 100  # Number of particles per explosion

# Define colors
def random_color():
    """Return a random bright color."""
    return (
        random.randint(128, 255),
        random.randint(128, 255),
        random.randint(128, 255)
    )

class Particle:
    def __init__(self, x, y, color, angle, speed):
        self.x = x
        self.y = y
        # Calculate velocity components
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.color = color
        self.lifetime = random.randint(50, 100)  # frames until the particle disappears

    def update(self):
        # Update particle position and apply gravity
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY  # gravity effect
        self.lifetime -= 1

    def draw(self, surface):
        if self.lifetime > 0:
            # Optionally, you can fade the particle based on lifetime
            fade = max(0, min(255, int(255 * (self.lifetime / 100))))
            color = (min(self.color[0], fade),
                     min(self.color[1], fade),
                     min(self.color[2], fade))
            pygame.draw.circle(surface, color, (int(self.x), int(self.y)), 3)

    def is_dead(self):
        return self.lifetime <= 0

class Firework:
    def __init__(self):
        # Start position at a random x along the bottom of the screen.
        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT
        self.color = random_color()
        # The rocket goes upward; choose a random upward speed.
        self.vy = random.uniform(-8, -12)
        self.exploded = False
        self.particles = []
        self.rocket_radius = 4

    def update(self):
        if not self.exploded:
            # Update the rocket's position.
            self.y += self.vy
            # Gravity slows the rocket upward.
            self.vy += GRAVITY
            # When the upward speed slows enough, trigger explosion.
            if self.vy >= -1:
                self.explode()
        else:
            # Update each particle after explosion.
            for particle in self.particles:
                particle.update()
            # Remove particles that have faded away.
            self.particles = [p for p in self.particles if not p.is_dead()]

    def explode(self):
        self.exploded = True
        # Create multiple particles radiating outward.
        for _ in range(PARTICLE_COUNT):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 6)
            self.particles.append(Particle(self.x, self.y, self.color, angle, speed))

    def draw(self, surface):
        if not self.exploded:
            # Draw the rocket as a small circle.
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.rocket_radius)
        else:
            # Draw all the particles.
            for particle in self.particles:
                particle.draw(surface)

    def is_dead(self):
        # The firework is dead if it has exploded and all particles have faded.
        return self.exploded and len(self.particles) == 0

def main():
    fireworks = []  # List to hold active fireworks
    running = True

    while running:
        clock.tick(60)  # 60 frames per second

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Optional: launch a new firework on mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                fireworks.append(Firework())

        # Occasionally launch a new firework automatically
        if random.random() < 0.02:  # roughly one firework every 50 frames
            fireworks.append(Firework())

        # Update fireworks
        for firework in fireworks:
            firework.update()

        # Remove fireworks that are finished
        fireworks = [f for f in fireworks if not f.is_dead()]

        # Clear the screen (fill with black)
        screen.fill((0, 0, 0))

        # Draw fireworks
        for firework in fireworks:
            firework.draw(screen)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
