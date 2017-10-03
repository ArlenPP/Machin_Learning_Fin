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

##		set up in and out condition		##

stophigh = 80
stoplow = 10

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
	print (my_porfolio.transation_list[i].id)



##==== start code ====##

#my_porfolio = porfolio(transation_Time)
my_test_result = test_result()
my_txff = txff()
f=open('../../option_roi_result.csv','w')
f.write("date,label,ROI_HF,ROI_LF,Buyprice,Sellprice_HF,Sellprice_LF\n")


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
win_LF = 0
Buyprice = 0
Sellprice_HF = 0
Sellprice_LF = 0

for i in range(0,(EndDayi-StartDayi)+1,1):
	
	if(my_test_result.label[i] == 1 and my_test_result.call[i] > CallPossible):
		
		Buyprice = my_txff.open[StartDayi+i]
		##==== high first ====##
		if((my_txff.high[StartDayi+i] - my_txff.open[StartDayi+i]) > stophigh):
			win_HF += stophigh -1 -(my_txff.open[StartDayi+i] +stophigh)*0.00002
			Sellprice_HF = my_txff.open[StartDayi+i]+stophigh

		elif((my_txff.open[StartDayi+i] - my_txff.low[StartDayi+i]) > stoplow):
			win_HF -= ((stoplow +1) + (my_txff.open[StartDayi+i] -stoplow)*0.00002)
			Sellprice_HF = my_txff.open[StartDayi+i]-stoplow

		else:
			win_HF += (my_txff.close[StartDayi+i] - my_txff.open[StartDayi+i])*0.99998 -1
			Sellprice_HF = my_txff.close[StartDayi+i]
		
		##==== low first ====##
		if((my_txff.open[StartDayi+i] - my_txff.low[StartDayi+i]) > stoplow):
			win_LF -= ((stoplow +1) + (my_txff.open[StartDayi+i] -stoplow)*0.00002)
			Sellprice_LF = my_txff.open[StartDayi+i] - stoplow

		elif((my_txff.high[StartDayi+i] - my_txff.open[StartDayi+i]) > stophigh):
			win_LF += stophigh -1 -(my_txff.open[StartDayi+i] +stophigh)*0.00002
			Sellprice_LF = my_txff.open[StartDayi+i]+stophigh

		else:
			win_LF += (my_txff.close[StartDayi+i] - my_txff.open[StartDayi+i])*0.99998 -1
			Sellprice_LF = my_txff.close[StartDayi+i]

		f.write(my_txff.date[StartDayi+i]+','+'call'+','+str(win_HF)+','+str(win_LF)+','+str(Buyprice)+','+str(Sellprice_HF)+','+str(Sellprice_LF)+'\n')
	
	elif(my_test_result.label[i] == -1 and my_test_result.put[i] > PutPossible):
		
		Buyprice = my_txff.open[StartDayi+i]
		##==== high first ====##
		if((my_txff.high[StartDayi+i] - my_txff.open[StartDayi+i]) > stoplow):
			win_HF -= ((stoplow +1) +(my_txff.open[StartDayi+i] + stoplow)*0.00002)
			Sellprice_HF = my_txff.open[StartDayi+i] + stoplow

		elif((my_txff.open[StartDayi+i] - my_txff.low[StartDayi+i]) > stophigh):
			win_HF += stophigh -1 -(my_txff.open[StartDayi+i] - stophigh)*0.00002
			Sellprice_HF = my_txff.open[StartDayi+i] - stophigh

		else:
			win_HF += (my_txff.open[StartDayi+i] - my_txff.close[StartDayi+i])*0.99998 -1
			Sellprice_HF = my_txff.close[StartDayi+i]

		##==== low first ====##
		if((my_txff.open[StartDayi+i] - my_txff.low[StartDayi+i]) > stophigh):
			win_LF += stophigh -1 -(my_txff.open[StartDayi+i] - stophigh)*0.00002
			Sellprice_LF = my_txff.open[StartDayi+i] - stophigh

		elif((my_txff.high[StartDayi+i] - my_txff.open[StartDayi+i]) > stoplow):
			win_LF -= ((stoplow +1) +(my_txff.open[StartDayi+i] + stoplow)*0.00002)
			Sellprice_LF = my_txff.open[StartDayi+i] + stoplow

		else:
			win_LF += (my_txff.open[StartDayi+i] - my_txff.close[StartDayi+i])*0.99998 -1
			Sellprice_LF = my_txff.close[StartDayi+i]

		f.write(my_txff.date[StartDayi+i]+','+'put'+','+str(win_HF)+','+str(win_LF)+','+str(Buyprice)+','+str(Sellprice_HF)+','+str(Sellprice_LF)+'\n')

print ('ROI_HF: '+str(win_HF))
print ('ROI_LF: '+str(win_LF))
print ('average:'+str((win_HF+win_LF)/2))
