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
        self.speed_x = 5  # Velocidad de movimiento horizontal
        self.speed_y = 4  # Velocidad de movimiento vertical (aumentada)
        self.direction_x = 1  # Dirección inicial horizontal (1 = derecha, -1 = izquierda)
        self.direction_y = 1  # Dirección inicial vertical (1 = abajo, -1 = arriba)

    def take_damage(self, amount):
        """Reduce la salud del jefe."""
        self.health -= amount
        print(f"El jefe ha recibido {amount} de daño. Salud restante: {self.health}")

    def move(self, screen_width, screen_height):
        """Mueve al jefe de lado a lado y más hacia arriba y abajo."""
        # Movimiento horizontal
        self.x += self.speed_x * self.direction_x
        if self.x <= 0 or self.x + self.rect.width >= screen_width:
            self.direction_x *= -1  # Cambia de dirección al llegar a los bordes horizontales

        # Movimiento vertical
        self.y += self.speed_y * self.direction_y
        if self.y <= 50 or self.y + self.rect.height >= screen_height // 2:  # Aumenta el rango vertical
            self.direction_y *= -1  # Cambia de dirección al llegar a los bordes verticales

        # Actualiza la posición del rectángulo
        self.rect.topleft = (self.x, self.y)

    def update_projectiles(self, screen_height):
        # Lógica para actualizar los proyectiles del jefe
        pass

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))  # Dibuja la imagen en la pantalla
        else:
            print("Advertencia: No se puede dibujar el jefe porque la imagen no está cargada.")
