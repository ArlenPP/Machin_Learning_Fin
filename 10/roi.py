#today buy today sell

import os
import csv
import math

test_result = open('./test-result','r')
#test_result = open('../../../output/10/test-result','r')
test = open('./test.csv','r')

labels= []
open = []
close = []

initmoney=0
finialmoney=0


for row in csv.DictReader(test_result, delimiter=' '):
	labels.append(float(row['labels']))
	


for row in csv.DictReader(test):
	open.append(float(row['Open']))
	close.append(float(row['Close']))

buymoney=0
sellmoney=0
savemoney=0
profit=0
x=0


for i in range (0,len(labels),1):

	if(profit>0):
		buymoney=sellmoney-profit+profit*3/4
		savemoney=savemoney+profit/4

	
		if(labels[i]==1):
			if(buymoney<open[i+10]):
				initmoney=initmoney-(open[i+10]-buymoney)
				buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
			number=1
			#number=math.floor(buymoney/open[i+10])
			sellmoney=number*close[i+40]
			profit=number*(close[i+40]-open[i+10])
			x=x+profit

			#y=y+profit/open[i+10]
			#here will have problem because the money actualy return at 30 days in the future

		elif(labels[i]==-1):

			if(buymoney<open[i+10]):
				initmoney=initmoney-(open[i+10]-buymoney)
				buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
			
			number=1
			#number=math.floor(buymoney/open[i+10])
			sellmoney=number*close[i+40]
			profit = number*(open[i+10]-close[i+40])
			x=x+profit
		
	else:
		buymoney=sellmoney
		if(labels[i]==1):
			if(buymoney<open[i+10]):
				initmoney=initmoney-(open[i+10]-buymoney)
				buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
			
			number=1
			#number=math.floor(buymoney/open[i+10])
			sellmoney=number*close[i+40]
			profit=number*(close[i+40]-open[i+10])
			x=x+profit
			
			#x=x+close[i+40]-open[i+10]

			#here will have problem because the money actualy return at 30 days in the future

		elif(labels[i]==-1):

			if(buymoney<open[i+10]):
				initmoney=initmoney-(open[i+10]-buymoney)
				buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
			
			number=1
			#number=math.floor(buymoney/open[i+10])
			sellmoney=number*open[i+10]
			profit = number*(open[i+10]-close[i+40])
			x=x+profit
	print(open[i+10],close[i+40],x)
	#print(x)
		#x=x+open[i+10]-close[i+40]
finialmoney=sellmoney+profit+sellmoney
'''
	buymoney=savemoney*3/4
	savemoney=savemoney/4
	print(open[i+10])
	#print(close[i+40])
	if(labels[i]==1):
		if(buymoney<open[i+10]):
			initmoney=initmoney-(open[i+10]-buymoney)
			buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
		
		number=math.floor(buymoney/open[i])
		buymoney=buymoney-number*open[i]
		sellmoney=number*close[i+40]
		x=x+close[i+40]-open[i]

		#here will have problem because the money actualy return at 30 days in the future

	elif(labels[i]==-1):

		if(buymoney<open[i+10]):
			initmoney=initmoney-(open[i+10]-buymoney)
			buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
		
		number=math.floor(buymoney/open[i+10])
		buymoney=buymoney-number*close[i+40]
		sellmoney=number*open[i+10]
		x=x+open[i+10]-close[i+40]
	savemoney=savemoney+buymoney+sellmoney
	
'''
initmoney=-initmoney
print(finialmoney/initmoney)
print(x)


