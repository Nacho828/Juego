import pygame

class Boss:
    def __init__(self, x, y, size=(300, 200)):
        self.x = x
        self.y = y
        self.width, self.height = size
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # Representa al jefe como un rectángulo
        self.health = 10  # Salud inicial del jefe
        self.projectiles = []

    def take_damage(self, amount):
        """Reduce la salud del jefe."""
        self.health -= amount
        print(f"El jefe ha recibido {amount} de daño. Salud restante: {self.health}")

    def move(self, screen_width):
        # Lógica para mover al jefe (puedes personalizar esto)
        pass

    def update_projectiles(self, screen_height):
        # Lógica para actualizar los proyectiles del jefe
        pass

    def draw(self, screen):
        # Dibuja el rectángulo que representa al jefe
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Rojo para el jefe
        print(f"Dibujando rectángulo del jefe en posición ({self.rect.left}, {self.rect.top})")
