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
        super().__init__(x, y)

    def move(self):
        """Mueve al oponente automáticamente."""
        self.rect.y += 2  # Baja 2 píxeles por frame
        if self.rect.top > 600:  # Si sale de la pantalla, reinicia su posición
            self.rect.y = -50

    def draw(self, screen):
        """Dibuja al oponente en la pantalla."""
        screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Prueba de Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fondo negro
    pygame.display.flip()  # Actualiza la pantalla

pygame.quit()




