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

stophigh = 80
stoplow = 2


##      set up porfolio condition       ##

transation_Time = 0
allin = 1
save = 0
StartDay = '2012/1/2'
EndDay = '2012/12/28'

##====	choose do Call or Put 1 is do 0 is not do 		====##
DoCall = 1
DoPut = 1


##==== define funtion ====##

def ROI():
	pass

##==== start code ====##

#my_porfolio = porfolio(transation_Time)
my_test_result = test_result()
my_txff = txff()
f=open('../../option_roi_result.csv','w')
f.write("date,roi\n")


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

win = 0

for i in range(0,(EndDayi-StartDayi)+1,1):
	if(my_test_result.label[i] == 1 and my_test_result.call[i] > 0.5):
		
		
		if((my_txff.high[StartDayi+i] - my_txff.open[StartDayi+i]) > stophigh):
			win += stophigh -1 -(my_txff.open[StartDayi+i] +stophigh)*0.00002

		elif((my_txff.open[StartDayi+i] - my_txff.low[StartDayi+i]) > stoplow):
			win -= ((stoplow +1) + (my_txff.open[StartDayi+i] -stoplow)*0.00002)



		
		else:
			win += (my_txff.close[StartDayi+i] - my_txff.open[StartDayi+i])*0.99998 -1
		f.write(my_txff.date[StartDayi+i]+','+str(win)+'\n')
	
	elif(my_test_result.label[i] == -1 and my_test_result.put[i] > 0.5):
		
		
		if((my_txff.high[StartDayi+i] - my_txff.open[StartDayi+i]) > stoplow):
			win -= ((stoplow +1) +(my_txff.open[StartDayi+i] + stoplow)*0.00002)
		
		elif((my_txff.open[StartDayi+i] - my_txff.low[StartDayi+i]) > stophigh):
			win += stophigh -1 -(my_txff.open[StartDayi+i] - stophigh)*0.00002

	
		else:
			win += (my_txff.open[StartDayi+i] - my_txff.close[StartDayi+i])*0.99998 -1

		f.write(my_txff.date[StartDayi+i]+','+str(win)+'\n')

print win


if(transation_Time == 0):
	pass
else:
	pass

