import datetime as dt
import csv

def get_date_str(date):
    return str(date)[0:10]

def get_begin_monday():
    if(dt.datetime.today().weekday() == 0):
        return dt.datetime.today()
    monday = dt.datetime.today() - dt.timedelta(days=dt.datetime.today().weekday())
    return monday

def get_end_sunday():
    if(dt.datetime.today().weekday() == 6):
        return dt.datetime.today()
    sunday = dt.datetime.today() + dt.timedelta(days = 6 - dt.datetime.today().weekday())
    return sunday

def get_week_range():
    day_list = []
    date = get_begin_monday()
    date_str = get_date_str(date)
    while(date_str != get_date_str(get_end_sunday())):
        day_list.append(date_str)
        date = date + dt.timedelta(days=1)
        date_str = get_date_str(date)
    day_list.append(get_date_str(get_end_sunday()))
    return day_list

def get_weekly_average():
    week_range = get_week_range()
    total_scores = 0
    num_scores = 0
    scores_file = open("output_files/scores.csv", 'r')
    reader = csv.DictReader(scores_file)
    for row in reader:
        if row['Date'] in week_range:
            total_scores += int(row['Score'])
            num_scores += 1
    scores_file.close()
    if num_scores == 0:
        return -1
    return total_scores / num_scores

def get_overall_average():
    total_scores = 0
    num_scores = 0
    scores_file = open("output_files/scores.csv", 'r')
    reader = csv.DictReader(scores_file)
    for row in reader:
        total_scores += int(row['Score'])
        num_scores += 1
    scores_file.close()
    if num_scores == 0:
        return -1
    return total_scores / num_scores

def print_weekly_average():
    begin_monday = get_date_str(get_begin_monday())
    end_sunday= get_date_str(get_end_sunday())
    avg = round(get_weekly_average(), 2)
    if(avg == -1):
        print("No scores found in output file!")
    else:
        print("This week, from " + begin_monday + " to " + end_sunday + ", your average was " + str(avg) + ".")

def print_overall_average():
    avg = round(get_overall_average(), 2)
    if(avg == -1):
        print("No scores found in output file!")
    else:
        print("Ever since you started using the recorder, your average score is " + str(avg) + ".")