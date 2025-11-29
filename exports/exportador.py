from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

class Exportador:
    def __init__(self, gestor):
        self.gestor = gestor

    def exportar_pdf(self, filename="glosario.pdf"):
        terminos = self.gestor.listar_todos()
        if not terminos:
            print("No hay términos para exportar.")
            return

        try:
            doc = SimpleDocTemplate(filename, pagesize=letter)
            styles = getSampleStyleSheet()
            story = []

            for t in terminos:
                texto = (
                    f"<b>Palabra:</b> {t.palabra}<br/>"
                    f"<b>Definición:</b> {t.definicion}<br/>"
                    f"<b>Ejemplos:</b> {', '.join(t.ejemplos)}<br/><br/>"
                )
                story.append(Paragraph(texto, styles["Normal"]))
                story.append(Spacer(1, 12))

            doc.build(story)
            print(f"PDF exportado correctamente como: {filename}")
        except Exception as e:
            print("❌ Error al exportar PDF:", e)
