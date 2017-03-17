import os
import csv


Open = []
Close = []
Volume = []
price_close= []
price_open = []
dowfile = open('./train _010115_to_103116.csv','r')

for row in csv.DictReader(dowfile):
	Open.append(str(float(row['Open'])))
	Close.append(str(float(row['Close'])))
	Volume.append(str(float(row['Volume'])))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
dowfile.close()


length = len(Open)
file = open('../output/test-data','w')

#start:lenghth-20,end:-1 but only to 0
for day in range(length-20,-1,-1):	
		
	
	if price_close[day-1]>price_open[day-1]:
		a='1'
	elif price_close[day-1]<=price_open[day-1]:
		a='-1'
	
	sma5 = 0
	for i in range(day,day+5,1):
		sma5 = price_close[i]+sma5
	sma5 = str(sma5/5)
	
	sma10 = 0
	for i in range(day,day+10,1):
		sma10 = price_close[i]+sma10
	sma10 = str(sma10)
	
	sma20 = 0
	for i in range(day,day+20,1):
		sma20 = price_close[i]+sma20
	sma20 = str(sma20/20)

	file.write(a+' 1:'+Open[day]+' 2:'+Close[day]+' 3:'+Volume[day]+' 4:'+sma5+' 5:'+sma10+' 6:'+sma20+'\n')