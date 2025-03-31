class Entity:
    """
    Clase base que representa cada elemento del juego.
    """

    def __init__(self, name, position):
        """
        Inicializa una nueva entidad.

        :param name: Nombre de la entidad.
        :param position: Posición de la entidad en el juego (x, y).
        """
        self.name = name
        self.position = position

    def move(self, dx, dy):
        """
        Mueve la entidad a una nueva posición.

        :param dx: Desplazamiento en el eje x.
        :param dy: Desplazamiento en el eje y.
        """
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def __str__(self):
        """
        Representación en cadena de la entidad.

        :return: Una cadena que describe la entidad.
        """
        return f"{self.name} at position {self.position}"