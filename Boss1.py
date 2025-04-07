import pygame
import math

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
        self.projectiles = []  # Lista para almacenar los proyectiles disparados
        self.shoot_cooldown = 30  # Tiempo entre disparos (en frames, reducido para mayor frecuencia)
        self.shoot_timer = 0  # Temporizador para controlar los disparos
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

    def update_projectiles(self, screen_width, screen_height):
        """Actualiza la posición de los proyectiles y elimina los que salen de la pantalla."""
        for projectile in self.projectiles[:]:
            projectile["y"] += projectile["dy"]  # Movimiento hacia abajo
            projectile["rect"].topleft = (projectile["x"], projectile["y"])
            if projectile["y"] > screen_height:  # Elimina proyectiles que salen de la pantalla
                self.projectiles.remove(projectile)

    def shoot(self):
        """Dispara dos balas hacia abajo desde el centro del jefe."""
        if self.shoot_timer == 0:
            center_x = self.rect.centerx
            bottom_y = self.rect.bottom

            speed = 10  # Velocidad de las balas

            # Crea las balas
            projectile1 = {
                "x": center_x - 20,  # Bala ligeramente a la izquierda del centro
                "y": bottom_y,
                "dx": 0,
                "dy": speed,
                "rect": pygame.Rect(center_x - 20, bottom_y, 10, 10)  # Tamaño de la bala
            }
            projectile2 = {
                "x": center_x + 20,  # Bala ligeramente a la derecha del centro
                "y": bottom_y,
                "dx": 0,
                "dy": speed,
                "rect": pygame.Rect(center_x + 20, bottom_y, 10, 10)  # Tamaño de la bala
            }

            # Agrega las balas a la lista de proyectiles
            self.projectiles.append(projectile1)
            self.projectiles.append(projectile2)

            # Reinicia el temporizador de disparo
            self.shoot_timer = self.shoot_cooldown

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))  # Dibuja la imagen en la pantalla
        else:
            print("Advertencia: No se puede dibujar el jefe porque la imagen no está cargada.")

        # Dibuja los proyectiles
        for projectile in self.projectiles:
            pygame.draw.rect(screen, (255, 255, 0), projectile["rect"])  # Amarillo para las balas

    def update(self, screen_width, screen_height):
        """Actualiza el movimiento, los disparos y los proyectiles del jefe."""
        self.move(screen_width, screen_height)
        self.update_projectiles(screen_width, screen_height)
        if self.shoot_timer > 0:
            self.shoot_timer -= 1
        self.shoot()
