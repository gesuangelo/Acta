from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors


def generate_acta_pdf(path="acta.pdf"):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=72,
    )

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleCentered",
            parent=styles["Title"],
            alignment=1,  # center
            spaceAfter=20,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionHeading",
            parent=styles["Heading2"],
            spaceBefore=20,
            spaceAfter=10,
        )
    )

    story = []
    story.append(Paragraph("Acta de Reunión", styles["TitleCentered"]))

    data = [
        ("Fecha:", "2024-08-30"),
        ("Lugar:", "Oficina Central"),
        ("Asistentes:", "Juan Pérez, María Gómez"),
    ]

    table = Table(data, colWidths=[80, 400])
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.gray),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F0F0F0")),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("ALIGN", (0, 0), (0, -1), "RIGHT"),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 12))

    story.append(Paragraph("Orden del Día", styles["SectionHeading"]))
    agenda = "1. Revisión de objetivos<br/>2. Presupuesto<br/>3. Planificación"  # using HTML breaks
    story.append(Paragraph(agenda, styles["Normal"]))

    story.append(Paragraph("Acuerdos", styles["SectionHeading"]))
    story.append(
        Paragraph(
            "Se acordó avanzar con el plan propuesto y revisar avances en la próxima reunión.",
            styles["Normal"],
        )
    )

    doc.build(story)


if __name__ == "__main__":
    generate_acta_pdf()
