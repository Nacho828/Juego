import pygame

class PlayerProjectile:
    def __init__(self, x, y, sprite_path="assets/player_projectile.png", speed=-10):
        # Cargar la imagen del proyectil del jugador
        self.image = pygame.image.load(sprite_path)
        self.image = pygame.transform.scale(self.image, (10, 20))  # Escalar la imagen si es necesario
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
    def __init__(self, x, y, sprite_path="assets/enemy_projectile.png", speed=5):
        # Cargar la imagen del proyectil del enemigo
        self.image = pygame.image.load(sprite_path)
        self.image = pygame.transform.scale(self.image, (10, 20))  # Escalar la imagen si es necesario
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed  # Velocidad del proyectil (hacia abajo)

    def move(self):
        """Mover el proyectil hacia abajo."""
        self.rect.y += self.speed

    def draw(self, screen):
        """Dibujar el proyectil en la pantalla."""
        screen.blit(self.image, self.rect)