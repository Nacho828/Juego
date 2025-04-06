import pygame

class Projectile:
    def __init__(self, x, y, color, speed=5):
        self.image = pygame.Surface((10, 20))  # Tamaño del proyectil
        self.image.fill(color)  # Color del proyectil
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed  # Velocidad del proyectil

    def move(self):
        """Mover el proyectil hacia abajo."""
        self.rect.y += self.speed

    def draw(self, screen):
        """Dibujar el proyectil en la pantalla."""
        screen.blit(self.image, self.rect)