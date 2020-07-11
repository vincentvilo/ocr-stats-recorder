import scores_calculator as sc
import matplotlib.pyplot as plt
import csv
import constants
from file_writer import str_to_list
import os

def clear():
    os.system('cls')

def print_instructions():
    print("=========================== INSTRUCTIONS ===========================")
    print("To see your average overall, press 1.")
    print("To see your average this week, press 2.")
    print("To view last three scores, press 3.")
    print("To view all scores in a line graph, press 4.")
    print("To exit out of the program, press 'ESC'.")
    print("The button must be pressed before/after starting a range session.")
    print("====================================================================\n")

def reset():
    clear()
    print_instructions()

def print_starting():
    print("RANGE RECORDER HAS STARTED!\n")

def print_ready():
    print("Recorder will start after shooting the start button.\n")

def print_range_found():
    print("RANGE DETECTED! WAITING TO FINISH RANGE...\n")

def print_completed_score(final_score):
    print("RANGE COMPLETED!")
    print("On that trial, you scored: " + str(final_score))

def print_weekly_average():
    begin_monday = sc.get_date_str(sc.get_begin_monday())
    end_sunday= sc.get_date_str(sc.get_end_sunday())
    avg = round(sc.get_weekly_average(), 2)
    if(avg == -1):
        print("No scores found in output file!")
    else:
        print("This week, from " + begin_monday + " to " + end_sunday + ", your average was " + str(avg) + ".")

def print_overall_average():
    avg = round(sc.get_overall_average(), 2)
    if(avg == -1):
        print("No scores found in output file!")
    else:
        print("Ever since you started using the recorder, your average score is " + str(avg) + ".")

def print_exiting():
    print("Recorder exiting...")

def plot_all_scores():
    x = []
    y = []
    with open(constants.ALLSCORES_PATH,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if (row[0] != 'Trial #'):
                x.append(int(row[0]))
                y.append(int(row[1]))
    plt.plot(x,y)
    plt.xlabel('Trial #')
    plt.ylabel('Score')
    plt.title('All scores from the Practice Range')
    print("Displaying graph...")
    print("Close the window to continue recording scores.")
    plt.show()

def print_previous_scores():
    line_list = []
    with open(constants.ALLSCORES_PATH, 'r') as open_file:
        num_trials = len(open_file.readlines()) - 1
        last_three = get_last_lines(constants.ALLSCORES_PATH, 3)
        for string in last_three:
            line_list.append(str_to_list(string, ",")) 
    print("Scores from the last three trials")
    for line in line_list:
        print("Trial #" + line[0] + ": " + line[1])

def get_last_lines(fname, n): 
    # opening file using with() method 
    # so that file get closed 
    # after completing work 
    line_list = []
    with open(fname) as file: 
        # loop to read iterate  
        # last n lines and print it 
        for line in (file.readlines() [-n:]): 
            if not('Score' in line):
                line_list.append(line.strip())
    return line_list