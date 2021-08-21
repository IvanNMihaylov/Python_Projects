import json
import csv
from pathlib import Path
import os.path
from datetime import datetime
from dateutil.tz import tzlocal

final_data = []


def data_file(city, date, temp):
    data = {}
    data['city'] = city                                                 # add city to the dictionary 'data'
    datetime_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")    # convert 'string' date to date 'object'
    local = datetime_object.astimezone(tzlocal())                       # convert date object to local date time
    data['date'] = str(local)                                           # add date to the dictionary 'data'
    if temp.upper().endswith('C'):                                      # check that the temperature is in Celsius
        celsius = ''
        for s in temp:                                                  # take only digits
            if s.isdigit():
                celsius += s
        cel = int(celsius)
        conv_c = (cel * 1.8) + 32                                       # formula for convert Celsius to Fahrenheit
        data['temp'] = "{:.0f}".format(conv_c) + "F"                    # add temp to the dictionary 'data'
    elif temp.upper().endswith('F'):                                    # check that the temperature is in Fahrenheit
        fahrenheit = ''
        for s in temp:                                                  # take only digits
            if s.isdigit():
                fahrenheit += s
        fahren = int(fahrenheit)
        conv_f = (fahren - 32) * 0.5556                                 # formula for convert Fahrenheit to Celsius
        data['temp'] = "{:.0f}".format(conv_f) + "C"                    # add temp to the dictionary 'data'
    return final_data.append(data.copy())


while True:
    file_name = input('Please write a file NAME: ')                     # ask user for file
    try:
        if os.path.isfile(file_name):                                   # check if there is a file
            if Path(file_name).suffix == '.csv':                        # for csv file
                with open(file_name) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
                    for row in csv_reader:
                        city = row[0]
                        date = row[1]
                        temp = row[2]
                        data_file(city, date, temp)                     # call the function data_file
                    break
            elif Path(file_name).suffix == '.json':                     # for json file
                f = open(file_name,)
                data = json.load(f)
                for i in data:
                    city = i['city']
                    date = i['date']
                    temp = i['temp']
                    data_file(city, date, temp)                         # call the function data_file
                f.close()
                break
    except:
        pass
    if file_name != file_name.endswith('.json'):                   # if the name is not found ask the user to try again
        print("Not found file! Please try again, add .json or .csv at the end of the name")

while True:
    end_file = input('Please write a FINAL file: ')
    if end_file.endswith('.json'):                                      # check file suffix from user input
        with open(end_file, 'w') as f:                                  # for json file
            f.write(json.dumps(final_data, ensure_ascii=False))         # add in json file
            break
    elif end_file.endswith('.csv'):                                     # check file suffix from user input
        keys = final_data[0].keys()
        with open(end_file, "w", newline="") as f:                      # for csv file
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(final_data)
            break
    else:
        print("Please write a file with suffix .json or .csv")


