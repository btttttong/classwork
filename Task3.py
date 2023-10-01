# Check which day on the next week  in Bangkok is going to be the hottest one.
# Use pprint, requests, datetime.

import requests
from  pprint import  pprint
from collections import Counter
from datetime import datetime

url = 'https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&hourly=temperature_2m,relativehumidity_2m&timezone=Asia%2FBangkok&forecast_days=14'


res = requests.get(url)
pprint(res.json())
values = res.json()

list_temperature_2m = values['hourly']['temperature_2m']
list_time = values['hourly']['time']
list_time_temp = {} #{time:temp,time:temp}
date_max_temp_dict = {}
print('--------------------')

def most_frequent_item_count(collection):
    if not collection:
        return 0
    counter = Counter(collection)
    most_common = counter.most_common(1)[0]
    return most_common

# Iterate over the list of time and temperature values.
for i in range(len(list_time)):
    # datei = datetime.fromisoformat(list_time[i])
    datei = list_time[i]
    tempi = list_temperature_2m[i]

    # If the date is not in the dictionary, add it with the maximum temperature.
    if datei not in date_max_temp_dict:
        date_max_temp_dict[datei] = tempi

    # If the maximum temperature for the date is less than the current maximum temperature,
    # update the maximum temperature for the date.
    elif date_max_temp_dict[datei] < tempi:
        date_max_temp_dict[datei] = tempi
# print('--------------------')
print(date_max_temp_dict)
hotday = most_frequent_item_count(date_max_temp_dict)
print('hottest day: ', datetime.fromisoformat(hotday[0]), ' temp: ', hotday[1])
