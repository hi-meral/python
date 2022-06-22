import csv
from math import ceil
import statistics

dict_from_csv = []

with open('./nyc_weather.csv', mode='r') as inp:
    reader = csv.reader(inp)
    next(reader)
    dict_from_csv = [int(rows[1]) for rows in reader]


x = statistics.mean(dict_from_csv[1:8])
y = max(dict_from_csv[1:11])

print(ceil(x))
print(y)
