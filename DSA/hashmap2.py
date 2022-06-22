import csv
from math import ceil
import statistics

dict_from_csv = {}

with open('./nyc_weather.csv', mode='r') as inp:
    reader = csv.reader(inp)
    next(reader)
    dict_from_csv = {rows[0]: int(rows[1]) for rows in reader}


print(dict_from_csv)

print(dict_from_csv["9-Jan"])
print(dict_from_csv["4-Jan"])
