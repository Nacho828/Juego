import pygame

class Boss:
    def __init__(self, x, y, image_path="assets/boss.png", size=(300, 200)):
        self.x = x
        self.y = y
        try:
            self.image = pygame.image.load(image_path)  # Carga la imagen del jefe
            self.image = pygame.transform.scale(self.image, size)  # Escala la imagen al tamaño deseado
        except pygame.error as e:
            print(f"Error al cargar la imagen del jefe: {e}")
            self.image = None
        self.rect = self.image.get_rect(topleft=(self.x, self.y)) if self.image else pygame.Rect(x, y, *size)
        self.health = 10  # Salud inicial del jefe
        self.projectiles = []
        self.speed = 10  # Velocidad de movimiento
        self.direction = 1  # Dirección inicial (1 = derecha, -1 = izquierda)

    def take_damage(self, amount):
        """Reduce la salud del jefe."""
        self.health -= amount
        print(f"El jefe ha recibido {amount} de daño. Salud restante: {self.health}")

    def move(self, screen_width):
        """Mueve al jefe de lado a lado."""
        self.x += self.speed * self.direction
        if self.x <= 0 or self.x + self.rect.width >= screen_width:
            self.direction *= -1  # Cambia de dirección al llegar a los bordes
        self.rect.topleft = (self.x, self.y)  # Actualiza la posición del rectángulo

    def update_projectiles(self, screen_height):
        # Lógica para actualizar los proyectiles del jefe
        pass

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))  # Dibuja la imagen en la pantalla
        else:
            print("Advertencia: No se puede dibujar el jefe porque la imagen no está cargada.")
