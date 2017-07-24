import os
import csv


abc = csv.DictReader(open('./1txff.csv','r'))

Open = []

for row in abc:
	Open.append(str(row['Open']))

print(Open)