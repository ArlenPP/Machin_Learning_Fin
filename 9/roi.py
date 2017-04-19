import os
import csv
import math

#test_result = open('./test-result','r')
test_result = open('../../../output/9/test-result','r')
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


buymoney=[]
sellmoney=[]
for x in xrange(1,31):
	buymoney.append(0)
	sellmoney.append(0)
	pass

walletmoney=0
savemoney=0
profit=0
x=0
y=0


for i in range (0,len(labels),1):

	walletmoney=walletmoney+sellmoney[i%30]

	if(labels[i]==-1):
		if(walletmoney<open[i+10]):
			outputmoney=outputmoney-(open[i+10]-walletmoney)
			walletmoney=walletmoney+(open[i+10]-walletmoney) 
		
		#number=1
		number=math.floor(walletmoney/open[i+10])
		buymoney[i%30]=number*open[i+10]
		walletmoney=walletmoney-buymoney[i%30]
		sellmoney[i%30]=number*close[i+40]
		
		profit=number*(close[i+40]-open[i+10])
		x=x+profit
		

	elif(labels[i]==1):
		if(walletmoney<open[i+10]):
			outputmoney=outputmoney-(open[i+10]-walletmoney)
			walletmoney=walletmoney+(open[i+10]-walletmoney)
			
		#number=1
		number=math.floor(walletmoney/open[i+10])
		buymoney[i%30]=number*open[i+10]
		walletmoney=walletmoney-buymoney[i%30]
		sellmoney[i%30]=number*(open[i+10]+open[i+10]-close[i+40])
		
		profit=number*(open[i+10]-close[i+40])
		x=x+profit

	y=y+profit/open[i+10]
	print(open[i+10],close[i+40],x,y,outputmoney,walletmoney)

finialmoney=walletmoney+sum(sellmoney)-(-outputmoney)

'''
buymoney=0
sellmoney=0
savemoney=0
profit=0
x=0
y=0
z=0

for i in range (0,len(labels),1):

	if(labels[i]==1):
		if(buymoney<open[i+10]):
			outputmoney=outputmoney-(open[i+10]-buymoney)
			buymoney=buymoney+(open[i]-buymoney) 
		
		#number=1
		number=math.floor(buymoney/open[i+10])
		buymoney=buymoney-number*open[i+10]
		sellmoney=number*close[i+40]
		buymoney=buymoney+sellmoney
		profit=number*(close[i+40]-open[i+10])
		x=x+profit
		

	elif(labels[i]==-1):
		if(buymoney<open[i+10]):
			outputmoney=outputmoney-(open[i+10]-buymoney)
			buymoney=open[i+10]   #=buymoney+(open[i]-buymoney) 
			
		#number=1
		number=math.floor(buymoney/open[i+10])
		buymoney=buymoney-number*open[i+10]
		sellmoney=number*(open[i+10]+open[i+10]-close[i+40])
		buymoney=buymoney+sellmoney
		profit=number*(open[i+10]-close[i+40])
		x=x+profit

	
	if(profit>0):
		buymoney=buymoney-profit+profit*3/4
		savemoney=savemoney+profit/4

	y=y+profit/open[i+10]
	z=z+1
	print(open[i+10],close[i+40],x,y,outputmoney,z)

finialmoney=buymoney+savemoney
'''

outputmoney=-outputmoney
print(finialmoney/outputmoney)
print "outputmoney =",outputmoney
print(x)


