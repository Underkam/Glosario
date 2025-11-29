import random
import matplotlib.pyplot as plt

class Quiz:
    def __init__(self, gestor):
        self.gestor = gestor

    def jugar(self):
        terminos = self.gestor.listar_todos()
        if not terminos:
            print("No hay términos para jugar.")
            return

        aciertos = 0
        errores = 0

        print("\n--- MODO QUIZ ---")
        print("Escribí 'salir' para terminar el juego en cualquier momento.\n")

        while True:
            termino = random.choice(terminos)
            print(f"Definición: {termino['definicion']}")
            respuesta = input("Palabra: ").strip()
            if respuesta.lower() == "salir":
                break
            if respuesta.lower() == termino['palabra'].lower():
                print("✅ Correcto!\n")
                aciertos += 1
            else:
                print(f"❌ Incorrecto! La palabra correcta era: {termino['palabra']}\n")
                errores += 1

        print(f"Juego terminado. Aciertos: {aciertos}, Errores: {errores}")

        # Gráfico de barras
        plt.figure(figsize=(8, 4))
        plt.subplot(1, 2, 1)
        plt.bar(["Aciertos", "Errores"], [aciertos, errores], color=["green", "red"])
        plt.title("Resultados del Quiz")

        # Gráfico circular
        plt.subplot(1, 2, 2)
        total = aciertos + errores
        if total == 0:
            total = 1
        plt.pie([aciertos, errores], labels=["Aciertos", "Errores"], colors=["green", "red"], autopct="%1.1f%%")
        plt.title("Proporción Aciertos/Errores")

        plt.tight_layout()
        plt.show()
