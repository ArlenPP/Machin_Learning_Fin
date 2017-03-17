import os
import csv


Open = []
Close = []
Volume = []
price_close= []
price_open = []
dowfile = open('./table_test.csv','r')

for row in csv.DictReader(dowfile):
	Open.append(str(float(row['Open'])))
	Close.append(str(float(row['Close'])))
	Volume.append(str(float(row['Volume'])))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
dowfile.close()


length = len(Open)
i = len(Open)-9
#print(length)
dowfile = open('./table_test.csv','r')
file = open('../output/test-data','w')

#start:lenghth-10,end:-1 but only to 0
for day in range(length-10,-1,-1):	
		
	i-=1
	if price_close[i]>price_open[i]:
		a='1'
	elif price_close[i]<=price_open[i]:
		a='-1'
	
	sma5 = str((price_close[i]+price_close[i+1]+price_close[i+2]+price_close[i+3]+price_close[i+4])/5)
	sma10 = str((price_close[i]+price_close[i+1]+price_close[i+2]+price_close[i+3]+price_close[i+4]+price_close[i+5]+price_close[i+6]+price_close[i+7]+price_close[i+8]+price_close[i+9])/10)
	

	file.write(a+' 1:'+Open[day]+' 2:'+Close[day]+' 3:'+Volume[day]+' 4:'+sma5+' 5:'+sma10+'\n')
	
dowfile.close()