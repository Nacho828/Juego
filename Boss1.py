from Oponent1 import Opponent
import pygame

class Boss(Opponent):
    def __init__(self, x, y, image_path, size=(300, 200)):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)  # Carga la imagen del jefe
        self.image = pygame.transform.scale(self.image, size)  # Escala la imagen al tamaño deseado
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.health = 10
        self.projectiles = []

    def special_attack(self):
        """Implementa un ataque especial del jefe final."""
        print("El jefe final realiza un ataque especial devastador.")

    def move(self, max_width):
        """Implementa la lógica de movimiento del jefe final."""
        self.rect.y += 1  # El jefe final se mueve más lento que los oponentes normales
        if self.rect.top > max_width:  # Si sale de la pantalla, reinicia su posición
            self.rect.y = -50

    def take_damage(self, damage):
        """
        Reduce la salud del jefe final al recibir daño.
        :param damage: Cantidad de daño recibido.
        """
        self.health -= damage
        print(f"El jefe final recibe {damage} de daño. Salud restante: {self.health}")
        if self.health <= 0:
            self.defeated()

    def defeated(self):
        """Lógica para manejar cuando el jefe final es derrotado."""
        print("¡El jefe final ha sido derrotado!")

    def draw(self, screen):
        """Dibuja al jefe final en la pantalla."""
        screen.blit(self.image, (self.x, self.y))  # Dibuja la imagen en la pantalla
