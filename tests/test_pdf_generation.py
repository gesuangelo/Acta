import os
import sys
from pathlib import Path

# Ensure the package is importable when running tests directly
sys.path.append(str(Path(__file__).resolve().parent.parent))
from acta_generator import generate_acta_pdf


def test_pdf_generation(tmp_path):
    pdf_path = tmp_path / "acta_test.pdf"
    generate_acta_pdf(str(pdf_path))
    assert pdf_path.exists()
    assert pdf_path.stat().st_size > 0
