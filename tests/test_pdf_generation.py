import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from acta_generator import generate_acta_pdf
from PyPDF2 import PdfReader


def test_pdf_generation(tmp_path):
    data = {
        "fecha": "2024-09-01",
        "lugar": "Sala de Juntas",
        "asistentes": ["Ana", "Luis"],
        "agenda": ["Revisión de presupuesto", "Planificación"],
        "acuerdos": "Se aprobó el presupuesto.",
    }
    pdf_path = tmp_path / "acta_test.pdf"
    generate_acta_pdf(str(pdf_path), data=data)
    assert pdf_path.exists()
    assert pdf_path.stat().st_size > 0

    reader = PdfReader(str(pdf_path))
    text = "".join(page.extract_text() or "" for page in reader.pages)
    assert "Sala de Juntas" in text
    assert "Ana" in text and "Luis" in text
    assert "Revisión de presupuesto" in text
    assert "Se aprobó el presupuesto." in text


class DummyForm(dict):
    """Simple form-like object that mimics ``request.form`` behavior."""

    def getlist(self, key):
        value = self[key]
        return value if isinstance(value, list) else [value]


def test_pdf_generation_from_form(tmp_path):
    form = DummyForm(
        {
            "fecha": ["2024-09-01"],
            "lugar": ["Sala de Juntas"],
            "asistentes[]": ["Ana", "Luis"],
            "agenda[]": ["Revisión de presupuesto", "Planificación"],
            "acuerdos": ["Se aprobó el presupuesto."],
        }
    )
    pdf_path = tmp_path / "acta_form.pdf"
    generate_acta_pdf(str(pdf_path), data=form)
    assert pdf_path.exists()
    reader = PdfReader(str(pdf_path))
    text = "".join(page.extract_text() or "" for page in reader.pages)
    assert "Sala de Juntas" in text
    assert "Ana" in text and "Luis" in text
    assert "Revisión de presupuesto" in text
    assert "Se aprobó el presupuesto." in text
