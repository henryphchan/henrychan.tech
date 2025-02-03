import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_firework(n_particles=100, speed=5):
    angles = np.linspace(0, 2 * np.pi, n_particles)
    radii = np.random.uniform(0.5, 1, n_particles)
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    velocities = speed * np.column_stack((x, y))
    return np.column_stack((x, y)), velocities

def update(frame, scat, particles, velocities, gravity):
    particles += velocities * 0.1
    velocities[:, 1] -= gravity * 0.1  # Gravity effect
    scat.set_offsets(particles)
    scat.set_alpha(max(0, 1 - frame / 50))  # Fade effect

def animate_firework():
    fig, ax = plt.subplots()
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_facecolor('black')
    
    particles, velocities = generate_firework(n_particles=150, speed=7)
    scatter = ax.scatter(particles[:, 0], particles[:, 1], c='yellow', s=20)
    
    ani = animation.FuncAnimation(fig, update, frames=50, fargs=(scatter, particles, velocities, 0.3), interval=50)
    plt.show()

animate_firework()
