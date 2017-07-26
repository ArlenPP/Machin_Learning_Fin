import csv
import os
import math
import datetime
from dateutil.relativedelta import relativedelta

##==== start code ====##

my_txff = csv.DictReader(open('./1txff.csv','r'))
Date = []
SMA5 = []
SMA10 = []
SMA20 = []
SMA60 = []
minus = []
Close = []

for row in my_txff:
	Date.append(str(row['Date']))
	SMA5.append(str(row['SMA5']))
	SMA10.append(str(row['SMA10']))
	SMA20.append(str(row['SMA20']))
	SMA60.append(str(row['SMA60']))
	Close.append(str(row['Close']))

for row in range(len(Date)):
	
	if((float(SMA5[row])-float(SMA10[row]))<0):
		minus.append(-1)
		continue
	if((float(SMA5[row])-float(SMA60[row]))>=0):
		minus.append(1)
	else:
		minus.append(-1)

print(len(minus))
print(len(Date))

for i in range(len(minus)-1):
	if(minus[i] == -1 and minus[i+1] == 1):
		print(Date[i+1])
		print('Buy')
	elif(minus[i] == 1 and minus[i+1] == -1):
		print(Date[i+1])
		print('Sell')

price1 = 0
price2 = 0
profolio1 = 0
profolio2 = 0
pro1buy = 0
pro2buy = 0


test = open('./abc.csv','w')
test.write('Date,profolio1,profolio2\n')


for a in range(len(Close)-1):
	if(minus[a] == -1 and minus[a+1] == 1):
		price1 = float(Close[a+1])
		pro1buy = 1
	elif(minus[a] == 1 and minus[a+1] == -1 and pro1buy == 1):
		profolio1 += (float(Close[a+1]) - price1)
		pro1buy = 0
		

	if(minus[a] == 1 and minus[a+1] == -1):
		price2 = float(Close[a+1])
		pro2buy = 1
	elif(minus[a] == -1 and minus[a+1] == 1 and pro2buy == 1):
		profolio1 += (float(Close[a+1]) - price2)
		pro2buy = 0
	test.write(Date[a+1]+','+str(profolio1)+','+str(profolio2)+'\n')

print(profolio1)
print(profolio2)




