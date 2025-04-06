import pygame
import random
from Boss1 import Boss
from Player1 import Player
from Oponent1 import Opponent
from projectile import Projectile

def draw_gradient(surface, color1, color2):
    """Dibujar un degradado en el fondo."""
    for y in range(surface.get_height()):
        ratio = y / surface.get_height()
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (surface.get_width(), y))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))  # Resolución Full HD
        pygame.display.set_caption("Juego Arcade")
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.score = 0
        self.lives = 3
        self.player = Player(375, 500)  # Posición inicial del jugador
        self.opponents = [
            Opponent(50, 50),   # Enemigo 1 más cerca del borde izquierdo
            Opponent(50, 45), # Enemigo 2 más abajo
            Opponent(60,50 )  # Enemigo 3 en una posición intermedia
        ]
        self.projectiles = []  # Lista para almacenar los proyectiles

    def start(self):
        """Inicia el juego."""
        self.is_running = True
        self.score = 0
        self.lives = 3
        print("Game started!")

    def update(self):
        """Actualizar la lógica del juego."""
        # Rellenar el fondo con un color sólido (negro en este caso)
        self.screen.fill((0, 0, 0))  # Color negro

        # Dibujar al jugador
        self.player.draw(self.screen)

        # Dibujar y mover a los enemigos
        for opponent in self.opponents:
            opponent.move(self.screen.get_width())  # Pasar el ancho de la pantalla
            opponent.draw(self.screen)

        # Dibujar y mover los proyectiles
        for projectile in self.projectiles:
            projectile.move()
            projectile.draw(self.screen)

        # Eliminar proyectiles que salgan de la pantalla
        self.projectiles = [p for p in self.projectiles if p.rect.bottom > 0]

        pygame.display.flip()

    def handle_events(self):
        """Manejar eventos del teclado y otros eventos."""
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # Disparar con la tecla 'E'
                    self.shoot()

    def shoot(self):
        """Crear un nuevo proyectil desde la posición del jugador."""
        projectile = Projectile(self.player.rect.centerx, self.player.rect.top)
        self.projectiles.append(projectile)

    def run(self):
        """Bucle principal del juego."""
        self.start()
        while self.is_running:
            self.handle_events()
            self.update()
            self.clock.tick(60)  # Limitar a 60 FPS
        pygame.quit()