from circleshape import *
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            degrees = random.uniform(20,50)
            new_direction1 = self.velocity.rotate(degrees)
            new_direction2 = self.velocity.rotate(-degrees)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            roid1 = Asteroid(self.position[0], self.position[1], new_radius)
            roid2 = Asteroid(self.position[0], self.position[1], new_radius)
            roid1.velocity = new_direction1 * 1.2
            roid2.velocity = new_direction2 * 1.2