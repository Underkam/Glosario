from models.termino import Termino

class GestorGlosario:
    def __init__(self, db):
        self.db = db

    def agregar(self, palabra, definicion, ejemplos):
        palabra = palabra.strip().upper()  # palabra en mayúsculas
        definicion = definicion.strip().capitalize()
        ejemplos = [e.strip().capitalize() for e in ejemplos if e.strip()]
        t = Termino(palabra, definicion, ejemplos)
        self.db.insertar_termino(t)

    def listar_todos(self):
        return self.db.listar_todos()  # ya ordenado en DB

    def buscar(self, palabra):
        palabra = palabra.strip().upper()
        return self.db.buscar_termino(palabra)

    def editar(self, palabra, nueva_def, nuevos_ej):
        palabra = palabra.strip().upper()
        nueva_def = nueva_def.strip().capitalize()
        nuevos_ej = [e.strip().capitalize() for e in nuevos_ej if e.strip()]
        self.db.editar_termino(palabra, nueva_def, nuevos_ej)

    def eliminar(self, palabra):
        palabra = palabra.strip().upper()
        self.db.eliminar_termino(palabra)
