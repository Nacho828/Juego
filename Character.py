from Entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        self.is_alive = True

    def move(self, direction):
        # Implement movement logic here
        print(f"Character moves {direction}")

    def shoot(self):
        # Implement shooting logic here
        print("Character shoots")

    def collide(self, damage):
        # Implement collision logic here
        self.lives -= damage
        if self.lives <= 0:
            self.is_alive = False
        print(f"Character collided and has {self.lives} lives left")
        
    def respawn(self):
        # Implement respawn logic here
        if not self.is_alive:
            self.lives = 3  # Reset lives to 3 or any other logic   
        self.is_alive = True
        print("Character respawned")
        
    def get_lives(self):
        """Return the number of lives left."""
        return self.lives
            

