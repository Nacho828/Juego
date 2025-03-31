class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        """Move the entity by dx and dy."""
        self.x += dx
        self.y += dy

    def draw(self, screen):
        """Draw the entity on the given screen."""
        screen.blit(self.image, (self.x, self.y))
        
    def get_position(self):
        """Return the current position of the entity."""
        return (self.x, self.y)

    def set_position(self, x, y):
        """Set the position of the entity."""
        self.x = x
        self.y = y

    def get_image(self):
        """Return the image of the entity."""
        return self.image
    
    def set_image(self, image):
        """Set the image of the entity."""
        self.image = image

            
    def get_rect(self):
        """Return the rect of the entity."""

            