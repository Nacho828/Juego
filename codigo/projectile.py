import pygame

class Projectile:
    def __init__(self, x, y):
        self.image = pygame.Surface((10, 20))  # Representación del proyectil
        self.image.fill((255, 255, 0))  # Color amarillo
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -10  # Velocidad hacia arriba

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)