import pygame
from Player1 import Player
from Boss1 import Boss
from Oponent1 import Opponent
from Projectile import Projectile

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

    def end_game(self):
        self.is_running = False
        print("Game ended!")
        print(f"Final score: {self.score}") 
        
    def get_score(self):    
        """Return the current score."""
        return self.score

    def set_score(self, score):
        """Set the current score."""
        self.score = score
    
    def __str__(self):
        """Return a string representation of the game state."""
        return (f"Game(is_running={self.is_running}, score={self.score}, "
                f"player={self.player}, opponents={self.opponents})")
        
    def convert_enemy_to_star(self):
        """Simulate converting an enemy to a star and increment the score."""
        if self.is_running:
            self.score += 1
            print("Enemy converted to star! Score increased.")
        else:
            print("Game is not running. Cannot convert enemy.")
    
    def lose_life(self):
        """Reduce the player's lives by one and check if the game should end."""
        if self.is_running:
            if self.lives > 0:
                self.lives -= 1
                print(f"Player hit! Lives remaining: {self.lives}")
                if self.lives == 0:
                    print("No lives left. Game over!")
                    self.end_game()
            else:
                print("No lives left. Game is already over.")
        else:
            print("Game is not running. Cannot lose a life.")
            
    def spawn_boss(self):
        """Spawn the final boss when the player defeats an enemy."""
        if self.is_running:
            self.opponent = Boss(speed=2)  # Boss moves twice as fast
            print("Final boss has appeared!")
        else:
            print("Game is not running. Cannot spawn boss.")