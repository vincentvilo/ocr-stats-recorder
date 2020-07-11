import datetime as dt
import os.path
from os import path
import os
import constants
import csv

def get_today_date():
    return str(dt.date.today())

def get_file_name():
    return str(get_today_date() + ".txt")

def get_file_path():
    return str(constants.OUT_DIRNAME + "/" + get_file_name())

def create_dir_files():
    if(not path.exists(constants.OUT_DIRNAME)):
        os.makedirs(constants.OUT_DIRNAME)
    file_path = constants.OUT_DIRNAME + "/" + get_file_name()
    if(not path.exists(file_path)):
        new_file = open(file_path, 'a')
        new_file.write("Scores\n")
        new_file.close()
    if(not path.exists(constants.ALLSCORES_PATH)):
        allscores_file = open(constants.ALLSCORES_PATH, 'a')
        allscores_file.write("Trial #,Score\n")
        allscores_file.close()

def write_score(score, filepath):
    new_file = open(filepath, 'a')
    if filepath == constants.ALLSCORES_PATH:
        new_file.write(str(file_len(filepath)) + "," + str(score) + "\n")
    else:
        new_file.write(str(score) + "\n")
    new_file.close()

def str_to_list(string, splitter): 
    return list(string.split(splitter))

def get_dict_from_csv(filepath):
    date_dict = {}
    csv_file = open(filepath, 'r')
    reader = csv.DictReader(csv_file)
    for row in reader:
        date = row['Date']
        scores = row['Scores']
        if row['Date'] != "-":
            date_dict[date] = str_to_list(scores, " ")
    return date_dict
    
def file_len(fname):
    new_file = open(fname)
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    new_file.close()
    return i + 1