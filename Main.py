from models.database import Database
from models.gestor_glosario import GestorGlosario
from exports.exportador import Exportador
from models.quiz import Quiz

def mostrar_menu():
    print("\n----- GLOSARIO OOP + SQLite -----")
    print("1. Agregar término")
    print("2. Buscar término")
    print("3. Listar todos")
    print("4. Editar término")
    print("5. Eliminar término")
    print("6. Exportar glosario (PDF)")
    print("7. Jugar Quiz")
    print("8. Salir")

def main():
    db = Database()
    gestor = GestorGlosario(db)
    exportador = Exportador(gestor)
    quiz = Quiz(gestor)

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        match opcion:
            case "1":
                palabra = input("Palabra: ")
                definicion = input("Definición: ")
                ejemplos = input("Ejemplos (separados por coma): ").split(",")
                gestor.agregar(palabra, definicion, [e.strip() for e in ejemplos])
                print("✔ Término agregado.")

            case "2":
                palabra = input("Buscar palabra: ")
                t = gestor.buscar(palabra)
                if t:
                    print(f"\n{t.palabra}: {t.definicion}")
                    for ej in t.ejemplos:
                        print(f" - {ej}")
                else:
                    print("❌ No encontrado.")

            case "3":
                terminos = gestor.listar_todos()
                for t in terminos:
                    print(f"{t.palabra}: {t.definicion}")
                    for ej in t.ejemplos:
                        print(f" - {ej}")

            case "4":
                palabra = input("Palabra a editar: ")
                nueva_def = input("Nueva definición: ")
                nuevos_ej = input("Nuevos ejemplos (coma): ").split(",")
                gestor.editar(palabra, nueva_def, [e.strip() for e in nuevos_ej])
                print("✔ Editado.")

            case "5":
                palabra = input("Palabra a eliminar: ")
                gestor.eliminar(palabra)
                print("✔ Eliminado.")

            case "6":
                exportador.exportar_pdf()

            case "7":
                quiz.jugar()

            case "8":
                print("Saliendo...")
                break

            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    main()
