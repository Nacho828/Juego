from Entity1 import Entity

class Shot(Entity):
    def __init__(self, x, y, speed):
        super().__init__(x, y)
        self.speed = speed

    def move(self):
        self.y += self.speed

    def hit_target(self, target):
        return self.x == target.x and self.y == target.y

    def __str__(self):
        return f"Shot at position ({self.x}, {self.y}) with speed {self.speed}"
    
    
    def get_speed(self):
        """Return the speed of the shot."""     
        return self.speed
    
    def set_speed(self, speed):     
        """Set the speed of the shot."""
        self.speed = speed
        print(f"Shot speed set to {self.speed}")    
        
    def get_position(self): 
        """Return the current position of the shot."""
        return (self.x, self.y)
    