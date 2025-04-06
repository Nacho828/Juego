import pygame
from Player1 import Player
from codigo.Boss1 import Boss
from Oponent1 import Opponent
from projectile import Projectile

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  # Tamaño de la ventana
        pygame.display.set_caption("Juego Arcade")
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.score = 0
        self.lives = 3
        self.player = Player(375, 500)  # Posición inicial del jugador
        self.opponents = [Opponent(100, 50), Opponent(300, 50), Opponent(500, 50)]  # Lista de enemigos
        self.projectiles = []  # Lista para almacenar los proyectiles

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
            opponent.draw(self.screen)
            opponent.move()

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