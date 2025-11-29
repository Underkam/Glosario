class Termino:
    def __init__(self, palabra, definicion, ejemplos=None):
        self.palabra = palabra
        self.definicion = definicion
        self.ejemplos = ejemplos or []
