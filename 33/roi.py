import os
import csv
import math

#test_result = open('./test-result','r')
test_result = open('../../../output/33/test-result','r')
test = open('./test.csv','r')

labels= []
open = []
close = []

for row in csv.DictReader(test_result, delimiter=' '):
	labels.append(float(row['labels']))
for row in csv.DictReader(test):
	open.append(float(row['Open']))
	close.append(float(row['Close']))

outputmoney=0
finialmoney=0


buymoney=0
sellmoney=0

walletmoney=0
savemoney=0
profit=0
x=0
y=0


for i in range (0,len(labels),1):

	walletmoney=walletmoney+sellmoney

	if(labels[i]==1):
		if(walletmoney<open[i+10]):
			outputmoney=outputmoney-(open[i+10]-walletmoney)
			walletmoney=walletmoney+(open[i+10]-walletmoney) 
		
		#number=1
		number=math.floor(walletmoney/open[i+10])
		buymoney=number*open[i+10]
		walletmoney=walletmoney-buymoney
		sellmoney=number*close[i+10]
		
		profit=number*(close[i+10]-open[i+10])
		x=x+profit
		

	elif(labels[i]==-1):
		if(walletmoney<open[i+10]):
			outputmoney=outputmoney-(open[i+10]-walletmoney)
			walletmoney=walletmoney+(open[i+10]-walletmoney)
			
		#number=1
		number=math.floor(walletmoney/open[i+10])
		buymoney=number*open[i+10]
		walletmoney=walletmoney-buymoney
		sellmoney=number*(open[i+10]+open[i+10]-close[i+10])
		
		profit=number*(open[i+10]-close[i+10])
		x=x+profit

	y=y+profit/open[i+10]
	print(open[i+10],close[i+10],x,y,outputmoney,walletmoney)

finialmoney=walletmoney+sellmoney-(-outputmoney)


outputmoney=-outputmoney
print(finialmoney/outputmoney)
print "outputmoney =",outputmoney
print(x)


