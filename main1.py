import os
os.environ["SDL_AUDIODRIVER"] = "dummy"  # Desactiva el audio

import pygame
from Game1 import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Prueba de Pygame")

    game = Game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fondo negro
        game.update()  # Actualiza la lógica del juego
        game.draw()    # Dibuja los elementos en la pantalla
        pygame.display.flip()  # Actualiza la pantalla

    pygame.quit()

if __name__ == "__main__":
    main()
