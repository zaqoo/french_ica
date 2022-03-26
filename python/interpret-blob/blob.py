import csv


def read_dictionary(file_name):
    f = open("dictionary/" + file_name)
    dico = f.read('\n').split()