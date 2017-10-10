import os
import csv
import datetime
from dateutil.relativedelta import relativedelta

tmp = csv.DictReader(open('./1min_txff_19980722_20171006.csv','r'))

f = open('./tmp.csv','w')

Date = []
Time = []
Open = []
High = []
Low = []
Close = []

number = 0




for row in tmp:
	#print(str(datetime.datetime.strptime(str(row['Date']), '%Y%m%d').strftime("%Y/%m/%d")))
	Date.append(str(row['Date']))
	Time.append(str(row['Time']))
	Open.append(str(row['Open']))
	High.append(str(row['High']))
	Low.append(str(row['Low']))
	Close.append(str(row['Close']))

for i in range(len(Open)):
	if(datetime.datetime.strptime(Date[i], '%Y/%m/%d') != datetime.datetime.strptime('20080102', '%Y%m%d')):
		continue
	number = i
	print('yes')
	break



f.write('Date,Time,Open,High,Low,Close\n')
for i in range(number,len(Date),1):
	f.write(str(Date[i])+','+str(Time[i])+','+str(Open[i])+','+str(High[i])+','+str(Low[i])+','+str(Close[i])+'\n')
	