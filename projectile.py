import pygame

class PlayerProjectile:
    def __init__(self, x, y, color=(255, 255, 0), speed=-10):  # Velocidad negativa para disparar hacia arriba
        self.image = pygame.Surface((10, 20))  # Tamaño del proyectil
        self.image.fill(color)  # Color del proyectil
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed  # Velocidad del proyectil

    def move(self):
        """Mover el proyectil hacia arriba."""
        self.rect.y += self.speed

    def draw(self, screen):
        """Dibujar el proyectil en la pantalla."""
        screen.blit(self.image, self.rect)


class EnemyProjectile:
    def __init__(self, x, y, color=(255, 0, 0), speed=5):  # Velocidad positiva para disparar hacia abajo
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