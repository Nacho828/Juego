import pygame
import random
from Boss1 import Boss
from Player1 import Player
from Oponent1 import Opponent
from projectile import PlayerProjectile

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
        self.screen = pygame.display.set_mode((1920,1080))
        pygame.display.set_caption("Juego Arcade")
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.score = 0
        self.lives = 3
        self.player = Player(960, 700)
        self.opponents = [
            Opponent(700, 150, "assets/enemy1.png", size=(150, 120)),
            Opponent(1200, 250, "assets/enemy2.png"),
            Opponent(200, 350, "assets/enemy3.png")
        ]
        self.projectiles = []  # Lista para almacenar los proyectiles del jugador

    def start(self):
        """Inicia el juego."""
        self.is_running = True
        self.score = 0
        self.lives = 3
        print("Game started!")

    def update(self):
        """Actualizar la lógica del juego."""
        self.screen.fill((0, 0, 0))  # Fondo negro

        # Dibujar al jugador
        self.player.draw(self.screen)

        # Dibujar y mover a los enemigos
        for opponent in self.opponents:
            opponent.move(self.screen.get_width())
            opponent.shoot()  # Hacer que los enemigos disparen
            opponent.update_projectiles(self.screen.get_height())  # Actualizar proyectiles
            opponent.draw(self.screen)

            # Detectar colisiones entre los proyectiles del enemigo y el jugador
            for projectile in opponent.projectiles:
                if projectile.rect.colliderect(self.player.rect):  # Si hay colisión
                    self.lives -= 1  # Reducir la vida del jugador
                    opponent.projectiles.remove(projectile)  # Eliminar el proyectil
                    if self.lives <= 0:
                        self.is_running = False  # Terminar el juego si el jugador muere

        # Dibujar y mover los proyectiles del jugador
        for projectile in self.projectiles:
            projectile.move()
            projectile.draw(self.screen)

            # Detectar colisiones entre proyectiles del jugador y enemigos
            for opponent in self.opponents:
                if projectile.rect.colliderect(opponent.rect):  # Si hay colisión
                    opponent.take_damage(1)  # Reducir la vida del enemigo
                    self.projectiles.remove(projectile)  # Eliminar el proyectil
                    break

        # Eliminar enemigos con vida <= 0
        self.opponents = [opponent for opponent in self.opponents if opponent.health > 0]

        pygame.display.flip()

    def handle_events(self):
        """Manejar eventos del teclado y otros eventos."""
        keys = pygame.key.get_pressed()
        self.player.move(keys)  # Mover al jugador con las teclas de dirección

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False  # Salir del juego
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # Si se presiona la tecla 'E'
                    self.shoot()  # Llamar al método para disparar

    def shoot(self):
        """Crear un nuevo proyectil desde la posición del jugador."""
        try:
            projectile = PlayerProjectile(self.player.rect.centerx, self.player.rect.top)  # Proyectil hacia arriba
            self.projectiles.append(projectile)
        except AttributeError as e:
            print(f"Error al disparar: {e}")

    def run(self):
        """Bucle principal del juego."""
        self.start()
        while self.is_running:
            self.handle_events()
            self.update()
            self.clock.tick(60)  # Limitar a 60 FPS
        pygame.quit()