from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors


def generate_acta_pdf(path="acta.pdf"):
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=50,
        rightMargin=50,
        topMargin=50,
        bottomMargin=50,
    )

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleCentered",
            parent=styles["Title"],
            alignment=1,  # center
            fontName="Helvetica-Bold",
            fontSize=16,
            textColor=colors.HexColor("#003366"),
            spaceAfter=20,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionHeading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            textColor=colors.HexColor("#005B9A"),
            spaceBefore=20,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyTextSmall",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
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
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#E6F2FF")),
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, colors.HexColor("#F5F5F5")]),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#333333")),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (0, -1), "RIGHT"),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 12))

    story.append(Paragraph("Orden del Día", styles["SectionHeading"]))
    agenda = "1. Revisión de objetivos<br/>2. Presupuesto<br/>3. Planificación"  # using HTML breaks
    story.append(Paragraph(agenda, styles["BodyTextSmall"]))

    story.append(Paragraph("Acuerdos", styles["SectionHeading"]))
    story.append(
        Paragraph(
            "Se acordó avanzar con el plan propuesto y revisar avances en la próxima reunión.",
            styles["BodyTextSmall"],
        )
    )

    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()

    with open(path, "wb") as f:
        f.write(pdf)

    return pdf


def main():
    generate_acta_pdf()
