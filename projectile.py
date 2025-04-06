import pygame

class Projectile:
    def __init__(self, x, y):
        # Cargar la imagen del proyectil
        self.image = pygame.image.load("assets/projectile.png")  # Ruta del sprite del disparo
        self.image = pygame.transform.scale(self.image, (50, 50))  # Escalar la imagen si es necesario
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -10  # Velocidad hacia arriba

    def move(self):
        """Mover el proyectil hacia arriba."""
        self.rect.y += self.speed

    def draw(self, screen):
        """Dibujar el proyectil en la pantalla."""
        screen.blit(self.image, self.rect)