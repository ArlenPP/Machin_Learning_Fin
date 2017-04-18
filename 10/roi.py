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
savemoney=0
x=0
#print(open[len(open)-len(labels)-29])
for i in range (0,len(labels),1):

	
	buymoney=savemoney*3/4
	savemoney=savemoney/4
	#print(open[i+10])
	#print(close[i+39])
	if(labels[i]==1):
		if(buymoney<open[i+10]):
			initmoney=initmoney-(open[i+10]-buymoney)
			buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
		
		number=1
		buymoney=buymoney-number*open[i]
		sellmoney=number*close[i+40]
		x=x+close[i+40]-open[i+10]

		#here will have problem because the money actualy return at 30 days in the future

	elif(labels[i]==-1):

		if(buymoney<open[i+10]):
			initmoney=initmoney-(open[i+10]-buymoney)
			buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
		
		number=1
		buymoney=buymoney-number*close[i+39]
		sellmoney=number*open[i+10]
		x=x+open[i+10]-close[i+39]
	savemoney=savemoney+buymoney+sellmoney
	'''
	buymoney=savemoney*3/4
	savemoney=savemoney/4
	print(open[i+10])
	#print(close[i+39])
	if(labels[i]==1):
		if(buymoney<open[i+10]):
			initmoney=initmoney-(open[i+10]-buymoney)
			buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
		
		number=math.floor(buymoney/open[i])
		buymoney=buymoney-number*open[i]
		sellmoney=number*close[i+39]
		x=x+close[i+39]-open[i]

		#here will have problem because the money actualy return at 30 days in the future

	elif(labels[i]==-1):

		if(buymoney<open[i+10]):
			initmoney=initmoney-(open[i+10]-buymoney)
			buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
		
		number=math.floor(buymoney/open[i+10])
		buymoney=buymoney-number*close[i+39]
		sellmoney=number*open[i+10]
		x=x+open[i+10]-close[i+39]
	savemoney=savemoney+buymoney+sellmoney
	
'''
finialmoney=savemoney
print(savemoney)
initmoney=-initmoney
print(initmoney)
print(finialmoney/initmoney)
print(x)
