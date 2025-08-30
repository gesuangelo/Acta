from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib import colors
from collections.abc import Mapping


def _normalize_data(data):
    """Normalize form-like data into a plain dictionary.

    Accepts regular dictionaries as well as objects similar to Flask's
    ``request.form`` which provide ``keys`` and ``getlist`` methods. Field
    names ending in ``[]`` are normalized by stripping the brackets.
    """

    if not data:
        return {}

    # Handle MultiDict / form-like objects
    if hasattr(data, "keys") and hasattr(data, "getlist"):
        normalized = {}
        for key in data.keys():
            values = data.getlist(key)
            base_key = key.rstrip("[]")
            normalized[base_key] = values if len(values) > 1 else values[0]
        return normalized

    # Fallback to a simple mapping
    if isinstance(data, Mapping):
        normalized = {}
        for key, value in data.items():
            base_key = key.rstrip("[]")
            normalized[base_key] = value
        return normalized

    return dict(data)


def generate_acta_pdf(path="acta.pdf", data=None):
    """Generate a meeting minute PDF using provided data.

    Parameters
    ----------
    path: str
        Output path for the generated PDF.
    data: dict | object | None
        Data source with keys ``fecha``, ``lugar``, ``asistentes``, ``agenda``
        and ``acuerdos``. It may be a regular dict or a form-like object. Missing
        keys default to empty strings/lists.
    """

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

    story = [Paragraph("Acta de Reunión", styles["TitleCentered"])]

    data = _normalize_data(data)
    fecha = data.get("fecha", "")
    lugar = data.get("lugar", "")
    asistentes = data.get("asistentes", "")
    if isinstance(asistentes, list):
        asistentes = ", ".join(str(a) for a in asistentes)

    table_data = [
        ("Fecha:", fecha),
        ("Lugar:", lugar),
        ("Asistentes:", asistentes),
    ]

    table = Table(table_data, colWidths=[80, 400])
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
    agenda_items = data.get("agenda", [])
    if isinstance(agenda_items, str):
        agenda_items = [agenda_items]
    agenda_text = "<br/>".join(
        f"{idx + 1}. {item}" for idx, item in enumerate(agenda_items)
    )
    story.append(Paragraph(agenda_text, styles["Normal"]))

    story.append(Paragraph("Acuerdos", styles["SectionHeading"]))
    acuerdos = data.get("acuerdos", "")
    story.append(Paragraph(acuerdos, styles["Normal"]))

    doc.build(story)


if __name__ == "__main__":
    sample_data = {
        "fecha": "2024-08-30",
        "lugar": "Oficina Central",
        "asistentes": ["Juan Pérez", "María Gómez"],
        "agenda": ["Revisión de objetivos", "Presupuesto", "Planificación"],
        "acuerdos": "Se acordó avanzar con el plan propuesto y revisar avances en la próxima reunión.",
    }
    generate_acta_pdf(data=sample_data)
