import pygame
from Character1 import Character  # Importa la clase Character desde Character.py

class Opponent(Character):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        """Mueve al oponente automáticamente."""
        self.rect.y += 2  # Baja 2 píxeles por frame
        if self.rect.top > 600:  # Si sale de la pantalla, reinicia su posición
            self.rect.y = -50

    def draw(self, screen):
        """Dibuja al oponente en la pantalla."""
        screen.blit(self.image, self.rect)




