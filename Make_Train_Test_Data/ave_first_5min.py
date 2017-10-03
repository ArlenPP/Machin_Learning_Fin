import csv
import os

one_min_txff = csv.DictReader(open('./database/1min_txff_19980722_20150325_part1.csv','r'))


ave_High = 0
ave_Low = 0
number = 0

Date = []
Open = []
High = []
Low = []

for row in one_min_txff:
	Date.append(row['Date'])
	Open.append(float(row['Open']))
	High.append(float(row['High']))
	Low.append(float(row['Low']))

startday = Date[0]

for i in range(0,len(Open),1):
	if(Date[i] != startday):
		start_open = Open[i]
		start_high = 0
		start_low = 99999

		for x in range(i,i+5,1):
			if(start_high < High[x]):
				start_high = High[x]
			if(start_low > Low[x]):
				start_low = Low[x]
		ave_High += (start_high - start_open)
		ave_Low += (start_open - start_low)

		startday = Date[i]
		number += 1

print('ave_high : '+str(ave_High/number))
print('ave_low : '+str(ave_Low/number))