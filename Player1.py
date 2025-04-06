import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))  # Representación del jugador
        self.image.fill((0, 255, 0))  # Color verde
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed