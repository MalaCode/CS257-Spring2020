import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict 


#################################
# This script creates datetime data from the csv file,
# then plots the number of confirmed cases vs the dates 
# of the reported cases. Finally, it counts the amount of times
# the number of cases has doubled. 
#
# For now just does it for one country or state/province.
##################################

def split(date): 
    return [char for char in date] 

def get_dates():
    x = []
    x_int = column_names[0][4:]
    for x_i in x_int:
        date_chars = split(x_i)
        year = 2020
        month = int(date_chars[0])
        day = ""
        day_chars = []
        if date_chars[3] == '/':
            day = int(date_chars[2])
        else:
            day_chars.append(date_chars[2])
            day_chars.append(date_chars[3])
            day = date_chars[2] + date_chars[3]
        day_int = int(day)
        x.append(datetime(year, month, day_int))
    return x
        
def get_country_data(country):
    y_temp= country_data[country]
    y = y_temp[2:]
    y_ints = []
    y_ints = list(map(int, y))
    return y_ints

def plot_data(x, y, country):
    plt.plot_date(x, y, linestyle='solid')
    title = country + ' COVID-19 Case Growth'
    plt.title(title)
    plt.ylabel('# Confirmed Cases')
    plt.xlabel('Dates')
    plt.show()
    return

def check_case_doubles(country, dates, cases):
    doubles = 0
    for i in range(0, len(cases)-1):
        if (cases[i+1] >= 2*cases[i]):
            doubles += 1
    print('The number of cases in ' + country + ' has doubled ' + str(doubles) + ' times.')

def visualize(place):
    x = get_dates()
    y = get_country_data(place)
    check_case_doubles(place, x, y)
    plot_data(x, y, place)

#################################################################

with open('time_series_covid19_confirmed_global.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    column_names = []
    country_data = defaultdict(list)
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            column_names.append(row)
        else:
            if row[0] == '':
                #if there's no state/province, the country is the dict key
                country_data[row[1]] = row[2:]
            #if there is a state/province, the state/province is the dict key
            country_data[row[0]] = row[2:]

# Replace Sweden with any state/province or any country without states/provinces
visualize('Sweden')

