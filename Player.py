from Character import Character

class Player(Character):
    def __init__(self, score=0, lives=3):
        super().__init__()
        self.score = score
        self.lives = lives

    def move(self, direction):
        # Implement movement logic here
        print(f"Player moves {direction}")

    def shoot(self):
        # Implement shooting logic here
        print("Player shoots")
        
    def collide(self, damage):
        # Implement collision logic here
        self.lives -= damage
        if self.lives <= 0:
            self.is_alive = False
        print(f"Player collided and has {self.lives} lives left")   
        
        
    def respawn(self):
        # Implement respawn logic here
        if not self.is_alive:
            self.lives = 3  # Reset lives to 3 or any other logic   
            
        self.is_alive = True
        print("Player respawned")   
        
    def get_score(self):        
        """Return the player's score."""
        return self.score   
    def __str__(self):
        return f"Player(score={self.score}, lives={self.lives}, is_alive={self.is_alive})"