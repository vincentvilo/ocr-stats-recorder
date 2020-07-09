import os.path
from os import path

def create_dir(dirname, filename):
    if(not path.exists(dirname)):
        os.makedirs(dirname)
        scores_file = open(dirname + "/" + filename, "w")
        scores_file.write("Range session #,Score\n")
        scores_file.close()

def write_score(score, filepath):
    scores_file = open(filepath, 'a')
    line_num = file_len(filepath)
    to_write = str(line_num) + "," + str(score) +"\n"
    scores_file.write(to_write)
    scores_file.close()

def file_len(fname):
    new_file = open(fname)
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    new_file.close()
    return i + 1