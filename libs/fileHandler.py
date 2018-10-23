# fileHandler.py
from pathlib import Path
from os import listdir
from os.path import isfile, join


'''
contains basic file handling methods
'''


def check_file(file):
    if file.exists():
        return True
    else:
        return False

def get_files(directory):
    list_files= [f for f in listdir(directory) if isfile(join(directory, f))]
    return list_files

def build_file_list(daterange):
    return
