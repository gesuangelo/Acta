# Generador de Acta

Este proyecto genera un documento PDF formal de un acta de reunión utilizando la librería [ReportLab](https://www.reportlab.com/).

## Requisitos

- Python 3.11+
- Dependencias listadas en `requirements.txt`

## Uso

```bash
pip install -r requirements.txt
python acta_generator.py  # genera un ejemplo con datos de muestra
```

También puedes importar la función y pasar tus propios datos:

```python
from acta_generator import generate_acta_pdf

data = {
    "fecha": "2024-09-01",
    "lugar": "Sala de Juntas",
    "asistentes": ["Ana", "Luis"],
    "agenda": ["Revisión de presupuesto", "Planificación"],
    "acuerdos": "Se aprobó el presupuesto.",
}
generate_acta_pdf("acta.pdf", data=data)

# También acepta estructuras tipo formulario (por ejemplo Flask request.form)
# con campos "agenda[]" o "asistentes[]" para valores múltiples.
# generate_acta_pdf("acta.pdf", data=request.form)
```

El archivo `acta.pdf` se generará en el directorio actual con la información proporcionada.

## Pruebas

Las pruebas utilizan `pytest`:

```bash
pytest
```
