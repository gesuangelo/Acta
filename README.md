# Generador de Acta

Este proyecto genera un documento PDF formal de un acta de reunión utilizando la librería [ReportLab](https://www.reportlab.com/).

## Requisitos

- Python 3.11+
- Dependencias listadas en `requirements.txt`

## Uso

```bash
pip install -r requirements.txt
python acta_generator.py
```

El archivo `acta.pdf` se generará en el directorio actual.

La función `generate_acta_pdf` también devuelve los bytes del PDF, lo que permite
enviarlo directamente en flujos de descarga o respuestas HTTP.

## Pruebas

Las pruebas utilizan `pytest`:

```bash
pytest
```
