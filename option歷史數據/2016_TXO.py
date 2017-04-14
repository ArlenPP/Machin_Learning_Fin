# coding=big5
import os
import csv

Date = []
Dateline = []
Strike_price = []
Callorput = [] 
Open = []
Close = []
high_price = []
open_price = []



optionfile = open('./2016/2016_opt_9.csv','r')
file = open('./2016_only_TXO/2016_9_TXO.csv','w')

for row in csv.DictReader(optionfile):
	if row['type']=='TXO':
		Date.append(str(row['date']))
		Dateline.append(str(row['dateline']))
		Strike_price.append(str(float(row['strike_price'])))
		Callorput.append(str(row['callorput']))
		Open.append(str(float(row['open'])))
		Close.append(str(float(row['close'])))
		open_price.append(float(row['open']))
		high_price.append(float(row['high']))
file.write("Date,Dateline,Strike_price,Callorput,Buyprice,Sellprice")
for i in range(1,len(Close),1):
	
	if high_price[i]>=open_price[i]*3:
		x=str(open_price[i]*3)
	else:
		x=Close[i]
	file.write(Date[i]+','+Dateline[i]+','+Strike_price[i]+','+Callorput[i]+','+Open[i]+','+x)
	file.write('\n')
file.close
optionfile.close()