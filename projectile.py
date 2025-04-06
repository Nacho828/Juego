import pygame

class PlayerProjectile:
    def __init__(self, x, y, sprite_path="assets/player_projectile.png", size=(80, 80), speed=-7):
        # Cargar la imagen del proyectil del jugador
        self.image = pygame.image.load(sprite_path)
        self.image = pygame.transform.scale(self.image, size)  # Escalar la imagen al tamaño especificado
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed  # Velocidad del proyectil (hacia arriba)

    def move(self):
        """Mover el proyectil hacia arriba."""
        self.rect.y += self.speed

    def draw(self, screen):
        """Dibujar el proyectil en la pantalla."""
        screen.blit(self.image, self.rect)


class EnemyProjectile:
    def __init__(self, x, y, sprite_path="assets/enemy_projectile.png", size=(50, 50), speed=4):
        # Cargar la imagen del proyectil del enemigo
        self.image = pygame.image.load(sprite_path)
        self.image = pygame.transform.scale(self.image, size)  # Escalar la imagen al tamaño especificado
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed  # Velocidad del proyectil (hacia abajo)

    def move(self):
        """Mover el proyectil hacia abajo."""
        self.rect.y += self.speed

    def draw(self, screen):
        """Dibujar el proyectil en la pantalla."""
        screen.blit(self.image, self.rect)