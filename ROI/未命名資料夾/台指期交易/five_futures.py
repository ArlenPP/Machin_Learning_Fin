#====   for typing chinese  ====#
#!/usr/bin/python
# coding=utf8

import sys
import os
import csv
import math
import datetime
import codecs
import re
from dateutil.relativedelta import relativedelta
from new_futures_class import test_result
from new_futures_class import txff
from new_futures_class import transation
from new_futures_class import profolio


Date = []
High = []
Low = []
Time = []


for row in five_raw:
	High.append(float(row['High']))
	Low.append(float(row['Low']))
	Date.append(row['Date'])
	Time.append(row['Time'])




##		set up in and out condition		##

year = '2016'
stophigh = 100
stoplow = 15

CallPossible = 0.35
PutPossible = 0.35

##      set up porfolio condition       ##

init_money = 100000
PriceOfFutures = 83000
#==== transation Time = 1 is day-trade ====#
transation_Time = 1
allin = 1
save = 0
StartDay = '2016/1/4'
EndDay = '2016/12/30'

##====	choose do Call or Put 1 is do 0 is not do 		====##
DoCall = 1
DoPut = 1


##==== define funtion ====##

def ROI():
	pass

my_porfolio = profolio(transation_Time,init_money)

for i in range(transation_Time):
	pass



five_raw = csv.DictReader(open('../../../Make_Train_Test_Data/database/five_'+year+'.csv','r'),delimiter=',')

##==== start code ====##

#my_porfolio = porfolio(transation_Time)
my_test_result = test_result()
my_txff = txff()
f=open('../../option_roi_result.csv','w')
f.write("date,label,ROI,Buyprice,SellTime\n")


##==== 	Enter Train Test START and End Day ====##
StartDayi = 0
EndDayi = 0

for i in range(len(my_txff.open)):
	if(my_txff.date[i] == StartDay):
		StartDayi = i
	if(my_txff.date[i] == EndDay):
		EndDayi = i
print (StartDayi,EndDayi,EndDayi-StartDayi)

##==== start roi ====##

win_HF = 0
Buyprice = 0
sellornot = 0
SellTime = 'null'


for i in range(0,(EndDayi-StartDayi)+1,1):
	
	if(my_test_result.label[i] == 1 and my_test_result.call[i] > CallPossible):
		
		Buyprice = my_txff.open[StartDayi+i]
		sellornot = 0

		Sellprice = 0
		for x in range(len(Date)):
			if(my_txff.date[StartDayi+i] == Date[x]):
				for y in range(59):
					if(High[x+y] - Buyprice > stophigh):
						win_HF += (stophigh -1)
						SellTime = Time[x+y]
						Sellprice = High[x+y]
						sellornot = 1
						print 'yyyyy'
						break
					elif(Buyprice - Low[x+y] > stoplow):
						win_HF -= (stoplow +1)
						SellTime = Time[x+y]
						sellornot = 1
						break

				break
		if(sellornot == 0):
			win_HF += (my_txff.close[StartDayi+i] - Buyprice -1)
			SellTime = '13:45'
			sellornot = 1

		f.write(my_txff.date[StartDayi+i]+','+'call'+','+str(win_HF)+','+str(Buyprice)+','+SellTime+','+str(Sellprice)+'\n')


	
	elif(my_test_result.label[i] == -1 and my_test_result.put[i] > PutPossible):
		
		Buyprice = my_txff.open[StartDayi+i]
		sellornot = 0
		
		for x in range(len(Date)):
			if(my_txff.date[StartDayi+i] == Date[x]):
				for y in range(59):
					if(High[x+y] - Buyprice > stoplow):
						win_HF -= (stoplow +1)
						SellTime = Time[x+y]
						sellornot = 1
						break
					elif(Buyprice - Low[x+y] > stophigh):
						win_HF += (stophigh -1)
						SellTime = Time[x+y]
						sellornot = 1
						break

				break
		if(sellornot == 0):
			win_HF += (Buyprice - my_txff.close[StartDayi+i] -1)
			SellTime = '13:45'
			sellornot = 1

		
		f.write(my_txff.date[StartDayi+i]+','+'put'+','+str(win_HF)+','+str(Buyprice)+','+SellTime+'\n')

print ('ROI: '+str(win_HF))

