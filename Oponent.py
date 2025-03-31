from Character import Character

class Opponent(Character):
    def __init__(self, name, health, is_star=False):
        super().__init__(name, health)
        self.is_star = is_star

    def move(self):
        # Implementar lógica de movimiento del oponente
        print(f"{self.name} se está moviendo.")

    def shoot(self):
        # Implementar lógica de disparo del oponente
        print(f"{self.name} está disparando.")

    def __str__(self):
        star_status = "estrella" if self.is_star else "no estrella"
        return f"Opponent({self.name}, Salud: {self.health}, Estado: {star_status})"
    
    

    def get_star_status(self):
        """Return if the opponent is a star."""
        return self.is_star             


    def set_star_status(self, is_star):
        """Set the star status of the opponent."""  
                                            
    
    
    
    