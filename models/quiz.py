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
        print("Escribí 'salir' para terminar.\n")

        while True:
            t = random.choice(terminos)
            print(f"Definición: {t.definicion}")
            respuesta = input("Palabra: ").strip()
            if respuesta.lower() == "salir":
                break
            if respuesta.upper() == t.palabra:
                print("✅ Correcto!\n")
                aciertos += 1
            else:
                print(f"❌ Incorrecto! La palabra correcta era: {t.palabra}\n")
                errores += 1

        print(f"Juego terminado. Aciertos: {aciertos}, Errores: {errores}")

        # Gráficos
        plt.figure(figsize=(8, 4))
        plt.subplot(1, 2, 1)
        plt.bar(["Aciertos", "Errores"], [aciertos, errores], color=["green", "red"])
        plt.title("Resultados del Quiz")

        plt.subplot(1, 2, 2)
        total = aciertos + errores or 1
        plt.pie([aciertos, errores], labels=["Aciertos", "Errores"], colors=["green", "red"], autopct="%1.1f%%")
        plt.title("Proporción Aciertos/Errores")

        plt.tight_layout()
        plt.show()
