from Oponent1 import Opponent
import pygame

class Boss(Opponent):
    def __init__(self, x, y,assets, size=(100, 100)):
        # Llama al constructor de la clase base Opponent
        super().__init__(x, y)
        self.image = pygame.image.load(assets).convert_alpha()  # Carga la imagen del jefe
        self.image = pygame.transform.scale(self.image, size)  # Ajusta el tamaño de la imagen del jefe
        self.rect = self.image.get_rect(topleft=(x, y))  # Define el rectángulo del jefe
        self.health = 100  # Salud inicial del jefe final

    def special_attack(self):
        """Implementa un ataque especial del jefe final."""
        print("El jefe final realiza un ataque especial devastador.")

    def move(self):
        """Implementa la lógica de movimiento del jefe final."""
        self.rect.y += 1  # El jefe final se mueve más lento que los oponentes normales
        if self.rect.top > 600:  # Si sale de la pantalla, reinicia su posición
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
        screen.blit(self.image, self.rect)
