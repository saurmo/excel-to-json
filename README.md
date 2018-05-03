# excel-to-json

Basado en https://github.com/XLSForm/pyxform y https://github.com/mvpdev/xls2xform/
Convierte un excel con formato http://xlsform.org/ a json, se le agrego una funcionalidad 
donde se puede pasar una carpeta con varios archivos de excel y los convierte cada uno a json

Versión de python 2.7

#Dependencias

* xlrd 
* unicodecsv 

#Run
Parametro 1 [Opción 1] = Una carpeta con archivos excel "test\xls" 
Parametro 1 [Opción 2] = Puede ser solo un archivo "ejemplo.xlsx"

Parametro 2 [Opción 1] = Carpeta existente donde se guardara el json "test\json" (En este caso el nombre del archivo .json es igual al nombre del excel)
Parametro 2 [Opción 2] = Nombre del archivo json y su ubicación "test/mi_ejemplo.json"

python src\xls2json.py parametro1 parametro2

python src\xls2json.py test\xls test\json

