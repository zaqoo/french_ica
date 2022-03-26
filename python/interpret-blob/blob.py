import csv
import pathlib
import os

def read_dictionary(file_name):
    f = open(os.path.realpath("..") + "/interpret-blob/dictionary/" + file_name)
    dico = f.read().split('\n')
    return dico

def read_profane_to_common(file_name):
    f = open(os.path.realpath("..") + "/interpret-blob/dictionary/" + file_name)
    tmp = f.read().split('\n')

    dico = {}
    for e in tmp:
        e2 = e.split(";")
        dico.update({e2[0] : e2[1]})
    return dico

def pro_to_com(str, dico):
    for key in dico:
        s = key.lower()
        print(key)
        str = str.replace(s, dico[key], 1)
    return str

def process_input(input):
    pro = read_profane_to_common("test.txt")
    return pro_to_com(input, pro)