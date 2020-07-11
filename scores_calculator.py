import datetime as dt
import csv
import constants

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
    for day in week_range:
        try:
            day_file = open(constants.OUT_DIRNAME + "/" + day + ".txt", 'r')
            for line in day_file.readlines():
                if line.strip() != 'Scores':
                    total_scores += int(line.strip())
                    num_scores += 1
            day_file.close()
        except FileNotFoundError:
            pass
    if num_scores == 0:
        return -1
    return total_scores / num_scores

def get_overall_average():
    total_scores = 0
    num_scores = 0
    scores_file = open(constants.ALLSCORES_PATH, 'r')
    reader = csv.DictReader(scores_file)
    for row in reader:
        total_scores += int(row['Score'])
        num_scores += 1
    scores_file.close()
    if num_scores == 0:
        return -1
    return total_scores / num_scores


