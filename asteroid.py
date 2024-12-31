import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self, dt):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        deviation = random.uniform(20, 50)
        random_angle = self.velocity.rotate(deviation)
        neg_random_angle = self.velocity.rotate(-deviation)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        
        first_asteroid.velocity = random_angle * 1.2
        second_asteroid.velocity = neg_random_angle * 1.2