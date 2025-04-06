import pygame

class Opponent:
    def __init__(self, x, y):
        self.image = pygame.Surface((100, 100))  # Crear un rectángulo temporal
        self.image.fill((255, 0, 0))  # Color rojo para el enemigo
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 3  # Velocidad de movimiento horizontal
        self.direction = 1  # 1 para derecha, -1 para izquierda

    def draw(self, screen):
        """Dibujar al enemigo en la pantalla."""
        screen.blit(self.image, self.rect)

    def move(self, screen_width):
        """Mover al enemigo horizontalmente de lado a lado."""
        self.rect.x += self.speed * self.direction

        # Cambiar de dirección al alcanzar los bordes de la pantalla
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.direction *= -1  # Invertir la dirección




