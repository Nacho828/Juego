import pygame
from Character1 import Character  # Importa la clase Character desde Character.py

class Opponent:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))  # Representación del enemigo
        self.image.fill((255, 0, 0))  # Color rojo
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.speed  




