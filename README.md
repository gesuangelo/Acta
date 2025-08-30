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

## Pruebas

Las pruebas utilizan `pytest`:

```bash
pytest
```
