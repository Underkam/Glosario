import sqlite3
from models.termino import Termino

class Database:
    def __init__(self, db_name="glosario.db"):
        self.conn = sqlite3.connect(db_name)
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS terminos (
                palabra TEXT PRIMARY KEY,
                definicion TEXT,
                ejemplos TEXT
            )
        ''')
        self.conn.commit()

    def insertar_termino(self, termino: Termino):
        cursor = self.conn.cursor()
        ejemplos_str = ",".join(termino.ejemplos)
        cursor.execute(
            "INSERT OR REPLACE INTO terminos (palabra, definicion, ejemplos) VALUES (?, ?, ?)",
            (termino.palabra, termino.definicion, ejemplos_str)
        )
        self.conn.commit()

    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT palabra, definicion, ejemplos FROM terminos ORDER BY palabra ASC")
        rows = cursor.fetchall()
        terminos = [Termino(row[0], row[1], row[2].split(',') if row[2] else []) for row in rows]
        return terminos

    def buscar_termino(self, palabra):
        cursor = self.conn.cursor()
        cursor.execute("SELECT palabra, definicion, ejemplos FROM terminos WHERE palabra=?", (palabra,))
        row = cursor.fetchone()
        if row:
            return Termino(row[0], row[1], row[2].split(',') if row[2] else [])
        return None

    def editar_termino(self, palabra, nueva_def, nuevos_ej):
        cursor = self.conn.cursor()
        ejemplos_str = ",".join(nuevos_ej)
        cursor.execute(
            "UPDATE terminos SET definicion=?, ejemplos=? WHERE palabra=?",
            (nueva_def, ejemplos_str, palabra)
        )
        self.conn.commit()

    def eliminar_termino(self, palabra):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM terminos WHERE palabra=?", (palabra,))
        self.conn.commit()
