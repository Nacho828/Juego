import pygame
import random
from projectile import EnemyProjectile

class Opponent:
    def __init__(self, x, y, sprite_path, size=(120, 120)):
        self.image = pygame.image.load(sprite_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 3
        self.direction = 1
        self.health = 10
        self.projectiles = []  # Lista para almacenar los proyectiles del enemigo
        self.shoot_cooldown = 0  # Temporizador para controlar el disparo (inicializado en 0)

    def draw(self, screen):
        """Dibujar al enemigo y sus proyectiles."""
        screen.blit(self.image, self.rect)
        for projectile in self.projectiles:
            projectile.draw(screen)

    def move(self, screen_width):
        """Mover al enemigo horizontalmente de lado a lado."""
        self.rect.x += self.speed * self.direction

        # Cambiar de dirección al alcanzar los bordes de la pantalla
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.direction *= -1  # Invertir la dirección

    def shoot(self):
        """Disparar un proyectil hacia abajo."""
        if self.shoot_cooldown == 0 and random.randint(1, 100) <= 5:  # Probabilidad de disparar (5%)
            projectile = EnemyProjectile(self.rect.centerx, self.rect.bottom)  # Proyectil rojo hacia abajo
            self.projectiles.append(projectile)
            self.shoot_cooldown = 30  # Establecer un tiempo de espera (60 fotogramas)

    def update_projectiles(self, screen_height):
        """Actualizar los proyectiles del enemigo."""
        if hasattr(self, 'shoot_cooldown') and self.shoot_cooldown > 0:  # Verificar si shoot_cooldown está definido
            self.shoot_cooldown -= 1  # Reducir el temporizador en cada fotograma

        for projectile in self.projectiles:
            projectile.move()
        # Eliminar proyectiles que salgan de la pantalla
        self.projectiles = [p for p in self.projectiles if p.rect.top < screen_height]

    def take_damage(self, damage):
        """Reducir la vida del enemigo."""
        self.health -= damage
        if self.health <= 0:
            self.health = 0  # Asegurarse de que no sea negativa




