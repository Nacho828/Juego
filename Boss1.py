from Oponent1 import Opponent

class Boss1(Opponent):
    def __init__(self, speed):
        self.speed = speed 

    def mover(self):
        # Lógica para mover al jefe final
        print(f"El Jefe Final se mueve a una velocidad de {self.velocidad}.")

    def atacar(self):
        # Lógica para el ataque del jefe final
        print("El Jefe Final lanza un ataque poderoso.")

    def __str__(self):
        return f"JefeFinal(velocidad={self.velocidad}, vida={self.vida})"


    def get_velocidad(self):    
        """Devuelve la velocidad del jefe final."""
        return self.velocidad
    
    def set_velocidad(self, velocidad):
        """Establece la velocidad del jefe final."""
        
        self.velocidad = velocidad
        print(f"Velocidad del Jefe Final establecida a {self.velocidad}")
        

                                                        