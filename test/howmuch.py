import os
import csv

price_close= []
price_open = []

dowfile = open('./train.csv','r')

for row in csv.DictReader(dowfile):
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))

number0 = 0.0
number1 = 0.0
numberminus1 = 0.0
total = 0.0

for day in range(5,len(price_open),1):
	total += 1
	if price_close[day]>(price_open[day]+100):
		number1 +=1
	elif (price_close[day]+100)<price_open[day]:
		numberminus1 += 1
	else :
		number0 += 1

print("number of 0 = "+str(number0)+' '+str(number0/total))
print("number of 1 = "+str(number1)+' '+str(number0*2/(number1)))
print("number of -1 = "+str(numberminus1)+' '+str(number0*2/(numberminus1)))
print("total = "+str(total))
