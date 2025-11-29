class GestorGlosario:
    def __init__(self, db):
        self.db = db

    def agregar(self, palabra, definicion, ejemplos):
        self.db.agregar(palabra, definicion, ejemplos)

    def buscar(self, palabra):
        return self.db.buscar(palabra)

    def listar_todos(self):
        return self.db.listar_todos()

    def editar(self, palabra, nueva_def, nuevos_ej):
        self.db.actualizar(palabra, nueva_def, nuevos_ej)

    def eliminar(self, palabra):
        self.db.eliminar(palabra)
