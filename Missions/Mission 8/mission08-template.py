#
# CS1010S --- Programming Methodology
#
# Mission 8 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)

    data = map(lambda x:x[1:], rows[1:])
    data = [tuple(map(int, tpl)) for tpl in data]
    rep_title = tuple(map(int, rows[0][1:]))
    age_title = tuple(map(int, map(lambda x:x[0], rows[1:])))

    return create_table(data, age_title, rep_title)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

print("## Q1 ##")
##Sit-up score of a 24-year-old who did 10 sit-ups.
print(access_cell(situp_table, 24, 10))    # 0

##Push-up score of a 18-year-old who did 30 push-ups.
print(access_cell(pushup_table, 18, 30))   # 16

# Run score of a 30-year old-who ran 12 minutes (720 seconds)
print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def pushup_score(pushup_table, age, pushup):
    min_rep = 1
    max_rep = 60
    
    if pushup < min_rep:
        pushup = min_rep
    elif pushup > max_rep:
        pushup = max_rep

    return access_cell(pushup_table, age, pushup)

def situp_score(situp_table, age, situp):
    min_rep = 1
    max_rep = 60
    
    if situp < min_rep:
        situp = min_rep
    elif situp > max_rep:
        situp = max_rep

    return access_cell(situp_table, age, situp)

def run_score(run_table, age, run):
    min_time = 510
    max_time = 1100
    
    if run < min_time:
        run = min_time
    elif run > max_time:
        run = max_time
    
    while access_cell(run_table, age, run) is None:
        run += 1

    return access_cell(run_table, age, run)

print("## Q2 ##")
print(pushup_score(pushup_table, 18, 61))   # 25
print(pushup_score(pushup_table, 18, 70))   # 25
print(situp_score(situp_table, 24, 0))      # 0

print(run_score(run_table, 30, 720))        # 36
print(run_score(run_table, 30, 725))        # 35
print(run_score(run_table, 30, 735))        # 35
print(run_score(run_table, 30, 500))        # 50
print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    #assuming score is int
    points = (51, 61, 75, 85)
    award = ("F", "P", "P$", "S", "G")
    
    for i in range(len(points)):
        if score < points[i]:
            return award[i]

    #goes here only if 85 or more points
    return award[4]

print("## Q3 ##")
print(ippt_award(50))     # F
print(ippt_award(51))     # P
print(ippt_award(61))     # P$
print(ippt_award(75))     # S
print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    pushup_pt = pushup_score(get_pushup_table(ippt_table), age, pushup)
    situp_pt = situp_score(get_situp_table(ippt_table), age, situp)
    run_pt = run_score(get_run_table(ippt_table), age, run)

    total = pushup_pt + situp_pt + run_pt

    return total, ippt_award(total)

print("## Q4 ##")
print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        pushup_t = int(pushup + days/rate_pushup)
        situp_t = int(situp + days/rate_situp)
        run_t = int(run - days/rate_run)

        result = ippt_results(ippt_table, age, pushup_t, situp_t, run_t)

        return pushup_t, situp_t, run_t, result
    return training_program

print("## Q5 ##")
tp = make_training_program(7, 3, 10)
print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########

def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        pushup_table = get_pushup_table(ippt_table)
        situp_table = get_situp_table(ippt_table)
        run_table = get_run_table(ippt_table)

        def points_ave(station_table, station_score_fn, reps, days, rate):
            station_score = station_score_fn(station_table, age, abs(reps))
            potential_reps = reps + int(days/rate)
            pot_station_score = station_score_fn(station_table, age, abs(potential_reps))
            pt_diff = pot_station_score - station_score
            
            return pt_diff/days

        if days <= 0 or (rate_pushup > days and rate_situp > days and rate_run > days):
            result = ippt_results(ippt_table, age, pushup, situp, run)
            return pushup, situp, run, result

        
      
        pushup_ave = points_ave(pushup_table, pushup_score, pushup, days, rate_pushup)
        situp_ave = points_ave(situp_table, situp_score, situp, days, rate_situp)
        run_ave = points_ave(run_table, run_score, -run, days, rate_run)
        print(pushup_ave, situp_ave, run_ave)
        
        max_pts = max(pushup_ave, situp_ave, run_ave)
        pushup_change, situp_change, run_change = 0,0,0
            
        if max_pts == pushup_ave:
            return tp_bonus(ippt_table, age, pushup + 1, situp, run, days - rate_pushup)
        elif max_pts == situp_ave:
            return tp_bonus(ippt_table, age, pushup, situp + 1, run, days - rate_situp)
        elif max_pts == run_ave:
            return tp_bonus(ippt_table, age, pushup, situp, run - 1, days - rate_run)
            
    return tp_bonus

tp_bonus = make_tp_bonus(7, 3, 10)

# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

print(tp_bonus(ippt_table, 25, 20, 30, 800, 30))      # (20, 40, 800, (58, 'P'))
print(tp_bonus(ippt_table, 25, 20, 30, 800, 2))       # (20, 30, 800, (52, 'P'))
