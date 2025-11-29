import sqlite3

class Database:
    def __init__(self, db_name="glosario.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS terminos (
                palabra TEXT PRIMARY KEY,
                definicion TEXT,
                ejemplos TEXT
            )
        ''')
        self.conn.commit()

    def agregar(self, palabra, definicion, ejemplos):
        self.cursor.execute(
            "INSERT OR REPLACE INTO terminos (palabra, definicion, ejemplos) VALUES (?, ?, ?)",
            (palabra, definicion, ",".join(ejemplos))
        )
        self.conn.commit()

    def buscar(self, palabra):
        self.cursor.execute("SELECT palabra, definicion, ejemplos FROM terminos WHERE palabra = ?", (palabra,))
        row = self.cursor.fetchone()
        if row:
            return {"palabra": row[0], "definicion": row[1], "ejemplos": row[2].split(",")}
        return None

    def listar_todos(self):
        self.cursor.execute("SELECT palabra, definicion, ejemplos FROM terminos")
        rows = self.cursor.fetchall()
        return [{"palabra": r[0], "definicion": r[1], "ejemplos": r[2].split(",")} for r in rows]

    def actualizar(self, palabra, nueva_def, nuevos_ej):
        self.cursor.execute(
            "UPDATE terminos SET definicion=?, ejemplos=? WHERE palabra=?",
            (nueva_def, ",".join(nuevos_ej), palabra)
        )
        self.conn.commit()

    def eliminar(self, palabra):
        self.cursor.execute("DELETE FROM terminos WHERE palabra=?", (palabra,))
        self.conn.commit()
