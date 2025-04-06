from Oponent1 import Opponent

class Boss(Opponent):
    def __init__(self, x, y):
        # Llama al constructor de la clase base Opponent
        super().__init__(x, y)
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


