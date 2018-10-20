# fileHandler.py
from pathlib import Path
from os import listdir
from os.path import isfile, join

#myfile=Path("fileHandler.py")

#if myfile.is_file():
#    print("File exists.")
#else:
#    print("Nothing found.")

#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

'''
contains basic file handling methods
'''


def check_file(file):
    file=Path(file)
    if file.is_file():
        return True
    else:
        return False

def get_files(directory):
    list_files= [f for f in listdir(directory) if isfile(join(directory, f))]
    return list_files
