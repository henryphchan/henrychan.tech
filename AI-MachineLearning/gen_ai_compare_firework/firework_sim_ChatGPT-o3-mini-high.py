import pygame
import random
import math

# Screen dimensions and frame rate
WIDTH, HEIGHT = 800, 600
FPS = 60

def random_color():
    """Return a random bright color."""
    return (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))

class Particle:
    """Represents a particle from an exploded firework with a tail."""
    def __init__(self, x, y, color, velocity, life):
        self.x = x
        self.y = y
        self.vx, self.vy = velocity
        self.color = color
        self.life = life  # Lifetime in frames
        self.trail = []  # List to store previous positions for the tail
        self.max_trail_length = 10  # Maximum length of the tail

    def update(self):
        """Update the particle's position, velocity, and its trail."""
        # Append current position to trail
        self.trail.append((self.x, self.y))
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)

        # Apply gravity to the particle's vertical velocity
        self.vy += 0.1
        # Update position
        self.x += self.vx
        self.y += self.vy
        # Decrease life
        self.life -= 1

    def draw(self, screen):
        """Draw the particle along with its tail."""
        if self.life > 0 and len(self.trail) > 0:
            # Base radius based on remaining life (for a fading size effect)
            current_radius = max(1, self.life // 5)
            # Draw the trail: older positions will be drawn fainter and smaller.
            trail_length = len(self.trail)
            for i, pos in enumerate(self.trail):
                # Compute a factor for fading based on the position's index in the trail.
                # The newest point (last in the list) has factor ~1.0.
                factor = (i + 1) / trail_length
                # Compute the radius for this segment of the tail.
                radius = max(1, int(current_radius * factor))
                # Fade the color by scaling the RGB components.
                faded_color = (
                    int(self.color[0] * factor),
                    int(self.color[1] * factor),
                    int(self.color[2] * factor)
                )
                pygame.draw.circle(screen, faded_color, (int(pos[0]), int(pos[1])), radius)

class Firework:
    """Represents a firework that launches upward and explodes into particles."""
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        # The rocket's initial upward velocity (negative means upward)
        self.vy = -random.uniform(7, 9)
        self.exploded = False
        self.particles = []

    def update(self):
        """Update the firework's state."""
        if not self.exploded:
            # Update the rocket's position
            self.y += self.vy
            # Gravity slows the rocket down
            self.vy += 0.1
            # When upward speed stops, explode!
            if self.vy >= 0:
                self.exploded = True
                self.explode()
        else:
            # Update each explosion particle
            for particle in self.particles:
                particle.update()
            # Remove particles that have faded out
            self.particles = [p for p in self.particles if p.life > 0]

    def explode(self):
        """Generate explosion particles in all directions."""
        num_particles = random.randint(30, 50)
        for _ in range(num_particles):
            # Random angle and speed for each particle
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 5)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            # Particle lifetime in frames
            life = random.randint(30, 50)
            self.particles.append(Particle(self.x, self.y, self.color, (vx, vy), life))

    def draw(self, screen):
        """Draw the firework or its explosion particles."""
        if not self.exploded:
            # Draw the rocket as a small circle
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)
        else:
            for particle in self.particles:
                particle.draw(screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Firework Simulation")
    clock = pygame.time.Clock()

    fireworks = []
    running = True

    while running:
        clock.tick(FPS)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Randomly add a new firework
        if random.randint(0, 50) == 0:
            x = random.randint(50, WIDTH - 50)
            fireworks.append(Firework(x, HEIGHT, random_color()))

        # Update all fireworks
        for firework in fireworks:
            firework.update()
        # Remove fireworks that have exploded and whose particles have all faded
        fireworks = [f for f in fireworks if not (f.exploded and len(f.particles) == 0)]

        # Clear the screen (black background)
        screen.fill((0, 0, 0))
        # Draw fireworks
        for firework in fireworks:
            firework.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
