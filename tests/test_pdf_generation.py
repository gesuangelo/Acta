import os
from acta_generator import generate_acta_pdf


def test_pdf_generation(tmp_path):
    pdf_path = tmp_path / "acta_test.pdf"
    generate_acta_pdf(str(pdf_path))
    assert pdf_path.exists()
    assert pdf_path.stat().st_size > 0
