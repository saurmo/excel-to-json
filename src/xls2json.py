"""
A Python script to convert excel files into JSON.
"""
from __future__ import print_function, unicode_literals
import json
import argparse
import codecs
import os
from errors import PyXFormError
from xls2json_backends import xls_to_dict, csv_to_dict
from workbook2json import workbook_to_json

def print_pyobj_to_json(pyobj, path=None):
    """
    dump a python nested array/dict structure to the specified file
    or stdout if no file is specified
    """
    if path:
        fp = codecs.open(path, mode="w", encoding="utf-8")
        json.dump(pyobj, fp=fp, ensure_ascii=False, indent=2)
        fp.close()
    else:
        print(json.dumps(pyobj, ensure_ascii=False, indent=2))

def get_filename(path):
    """
    Get the extensionless filename from a path
    """
    return os.path.splitext((os.path.basename(path)))[0]

def parse_file_to_workbook_dict(path, file_object=None):
    """
    Given a xls or csv workbook file use xls2json_backends to create
    a python workbook_dict.
    workbook_dicts are organized as follows:
    {sheetname : [{column_header : column_value_in_array_indexed_row}]}
    """
    (filepath, filename) = os.path.split(path)    
    if not filename:
        raise PyXFormError("No filename.")

    (shortname, extension) = os.path.splitext(filename)
    if not extension:
        raise PyXFormError("No extension.")

    if extension == ".xls" or extension == ".xlsx":
        json_dict_xls=xls_to_dict(file_object if file_object is not None else path)
        return json_dict_xls
    elif extension == ".csv":
        return csv_to_dict(file_object if file_object is not None else path)
    else:
        raise PyXFormError("File was not recognized")

def parse_file_to_json(path, default_name=None, default_language=u"default", warnings=None, file_object=None):
    """
    A wrapper for workbook_to_json
    """
    if warnings is None:
        warnings = []
    workbook_dict = parse_file_to_workbook_dict(path, file_object)
    if default_name is None:
        default_name = unicode(get_filename(path))
    return workbook_to_json(workbook_dict, default_name, default_language, warnings)

def _create_parser():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path_in", help="Path (Filer or Folder) to the Excel XSLX file with the XLSForm definition.")
    parser.add_argument("path_out", help="Folder path to save the output to.")
    return parser

def run_file_to_json(file_in, output):    
    filename = unicode(get_filename(file_in))
    json_survey = parse_file_to_json(file_in, filename)
    if os.path.isdir(output):
        json_out=output+"/"+filename+".json"
    else:
        json_out=output.split(".")[0]+".json"
    print_pyobj_to_json(json_survey, json_out)
 
def run_folder_to_json(folder_in, folder_out):
    files=os.listdir(folder_in)
    out = folder_out
    if os.path.isdir(folder_out)==False:
        out=folder_out.split(".")[0]
    for f in files:
        file_in = folder_in + "/" + f
        run_file_to_json(file_in, out)

def main_cli():
    parser = _create_parser()
    args = parser.parse_args()
    path_in = args.path_in
    path_out = args.path_out
    if os.path.isdir(path_in):
        run_folder_to_json(path_in, path_out)
    else:
        run_file_to_json(path_in, path_out)
    print("Conversion complete")

if __name__ == "__main__":
    main_cli()
    