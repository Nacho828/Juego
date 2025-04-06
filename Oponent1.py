import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Tamaño del personaje
        self.image.fill((255, 0, 0))  # Color rojo
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Opponent(Character):
    def __init__(self, x, y):
        # Pasa los argumentos correctos al constructor de la clase base
        super().__init__(x, y)

    def move(self):
        """Mueve al oponente automáticamente."""
        self.rect.y += 2  # Baja 2 píxeles por frame
        if self.rect.top > 600:  # Si sale de la pantalla, reinicia su posición
            self.rect.y = -50

    def draw(self, screen):
        """Dibuja al oponente en la pantalla."""
        screen.blit(self.image, self.rect)




