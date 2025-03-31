class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if self.is_running:
            print("Game is updating...")
            # Add game logic here
        else:
            print("Game is not running.")

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
                f"player={self.player}, opponent={self.opponent})")
        
    def convert_enemy_to_star(self):
        """Simulate converting an enemy to a star and increment the score."""
        if self.is_running:
            self.score += 1
            print("Enemy converted to star! Score increased.")
        else:
            print("Game is not running. Cannot convert enemy.")