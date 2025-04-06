import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, lives):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Tamaño del personaje
        self.image.fill((0, 255, 0))  # Color verde
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.lives = lives

class Player(Character):
    def __init__(self, x, y):
        # Pasa el argumento 'lives' al constructor de la clase base
        super().__init__(x, y, lives=3)

    def move(self, dx, dy):
        """Mueve al jugador en la dirección especificada."""
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        """Dibuja al jugador en la pantalla."""
        screen.blit(self.image, self.rect)