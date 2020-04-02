# EXCEL A JSON (PYTHON 2.7)

Basado en https://github.com/XLSForm/pyxform y https://github.com/mvpdev/xls2xform/
Convierte un excel con formato http://xlsform.org/ a json, se le agrego una funcionalidad
donde se puede pasar una carpeta con varios archivos de excel y los convierte cada uno a json

Nota: Se utiliza python con versión de python 2.7

## Dependencias

Las dependias que se deben de tener instaladas en python con el pip son:

- `pip install xlrd`
- `pip install unicodecsv`

## ¿Cómo ejecutar el proyecto?

### Primera opción: Ejecutar una carpeta con archivos excel

```python
    python src\xls2json.py ../../pruebas/archivos parametro2
```

```python
    python src\xls2json.py parametro1 parametro2
```

1. parametro1 es la ruta y el nombre de la carpeta que contiene los excel.
2. parametro2 es la ruta y el nombre de la carpeta donde se van a guardar los json

### Primera opción: Ejecutar una carpeta con archivos excel

```
    python src\xls2json.py ../../pruebas/archivos-excel ../../resultado/archivos-json
```

```
    python src\xls2json.py parametro1 parametro2
```

1. parametro1 es la ruta y el nombre de la carpeta que contiene los excel.
2. parametro2 es la ruta y el nombre de la carpeta donde se van a guardar los json

### Segunda opción: Ejecutar un archivo excel

```
    python src\xls2json.py ../../pruebas/archivo-excel.xlsx ../../resultado/archivo.json
```

```
    python src\xls2json.py parametro1 parametro2
```

1. parametro1 es la ruta y el nombre del archivo excel.
2. parametro2 es la ruta y el nombre del archivo json que se generará
