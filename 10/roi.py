#today buy today sell

import os
import csv
import math

test_result = open('../../../output/10/test-result','r')
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


for i in range (len(open)-len(labels),len(labels)-30,1):
	buymoney=savemoney*3/4
	savemoney=savemoney/4

	if(labels[i]==1):
		if(buymoney<open[i]):
			initmoney=initmoney-(open[i]-buymoney)
			buymoney=open[i]   #=buymoney+(open[i]-buymoney) 
		
		number=math.floor(buymoney/open[i])
		buymoney=buymoney-number*open[i]
		sellmoney=number*close[i+30]
		#here will have problem because the money actualy return at 30 days in the future

	elif(labels[i]==-1):

		if(buymoney<open[i]):
			initmoney=initmoney-(open[i]-buymoney)
			buymoney=open[i]   #=buymoney+(open[i]-buymoney) 
		
		number=math.floor(buymoney/open[i])
		buymoney=buymoney-number*close[i+30]
		sellmoney=number*open[i]

	savemoney=buymoney+sellmoney

finialmoney=savemoney
initmoney=-initmoney
print(finialmoney/initmoney)