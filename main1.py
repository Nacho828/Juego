import os
os.environ["SDL_AUDIODRIVER"] = "dummy"  # Desactiva el audio

try:
    from Game1 import Game
except ImportError:
    print("Error: No se pudo importar 'Game' desde 'Game1'. Verifica que el archivo 'Game1.py' exista y contenga la clase 'Game'.")
    raise


def main():
    print("¡Bienvenido al juego!")
    # Aquí puedes agregar la lógica principal de tu juego
    game = Game()
    game.start()

if __name__ == "__main__":
    main()  # Llama correctamente a la función main
