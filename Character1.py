import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Tamaño del personaje
        self.image.fill((0, 255, 0))  # Color verde
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Establece la posición inicial del personaje



