import pygame, random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0,1)
    
    def draw(self, screen):
        return pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 5
        random_angle = random.uniform(20, 50)
        new1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new1.velocity = self.velocity.rotate(random_angle) * ASTEROID_SPEED_INCREASE
        new2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new2.velocity = self.velocity.rotate(-random_angle) * ASTEROID_SPEED_INCREASE
        
        if self.radius <= ASTEROID_MAX_RADIUS:
            return 2
        if self.radius == ASTEROID_MAX_RADIUS:
            return 1
