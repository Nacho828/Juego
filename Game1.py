import pygame
from Player1 import Player
from Boss1 import Boss
from Oponent1 import Opponent

class Game:
    def __init__(self):
        pygame.init()
        print("Pygame inicializado correctamente.")  # Mensaje de depuración
        self.screen = pygame.display.set_mode((800, 600))  # Ventana de 800x600
        pygame.display.set_caption("Mi Juego con Pygame")
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.lives = 3
        self.player = Player(400, 500)  # Posición inicial del jugador
        self.opponent = Opponent(400, 100)  # Posición inicial del oponente
        self.is_running = False

    def start(self):
        """Inicia el bucle principal del juego."""
        self.is_running = True
        self.score = 0
        print("Game started!")
        while self.running:
            self.handle_events()  # Maneja los eventos del jugador
            self.update()         # Actualiza la lógica del juego
            self.draw()           # Dibuja los elementos en la pantalla
            self.clock.tick(60)   # Limita a 60 FPS

        pygame.quit()

    def handle_events(self):
        """Maneja los eventos del juego, como teclas presionadas o cerrar la ventana."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Cerrar ventana
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(-5, 0)  # Mueve al jugador a la izquierda
                elif event.key == pygame.K_RIGHT:
                    self.player.move(5, 0)   # Mueve al jugador a la derecha
                elif event.key == pygame.K_SPACE:
                    self.convert_enemy_to_star()  # Convierte al enemigo en estrella

    def update(self):
        """Actualiza la lógica del juego."""
        if self.is_running:
            self.opponent.move()  # Mueve al oponente
            if self.check_collision(self.player, self.opponent):
                self.lose_life()  # Reduce las vidas si hay colisión

    def draw(self):
        """Dibuja los elementos del juego en la pantalla."""
        self.screen.fill((0, 0, 0))  # Fondo negro
        self.player.draw(self.screen)  # Dibuja al jugador
        self.opponent.draw(self.screen)  # Dibuja al oponente

        # Dibuja el puntaje y las vidas
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))

        pygame.display.flip()  # Actualiza la pantalla

    def check_collision(self, player, opponent):
        """Verifica si el jugador colisiona con el oponente."""
        return player.rect.colliderect(opponent.rect)

    def end_game(self):
        """Termina el juego."""
        self.is_running = False
        print("Game ended!")
        print(f"Final score: {self.score}")

    def convert_enemy_to_star(self):
        """Simula convertir un enemigo en una estrella y aumenta el puntaje."""
        if self.is_running:
            self.score += 1
            print("Enemy converted to star! Score increased.")
        else:
            print("Game is not running. Cannot convert enemy.")

    def lose_life(self):
        """Reduce las vidas del jugador y verifica si el juego debe terminar."""
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