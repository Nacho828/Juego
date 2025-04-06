import pygame
from Game1 import Game

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Juego Arcade")
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.score = 0
        self.lives = 3  # Vida inicial del jugador
        self.player = Player(375, 500)
        self.opponents = [
            Opponent(100, 50, "assets/enemy1.png"),
            Opponent(300, 100, "assets/enemy2.png"),
            Opponent(500, 150, "assets/enemy3.png")
        ]
        self.projectiles = []  # Lista para almacenar los proyectiles del jugador

def main():
    print("¡Bienvenido al juego!")
    game = Game()
    game.run()  # Ejecuta el bucle principal del juego

if __name__ == "__main__":
    main()
