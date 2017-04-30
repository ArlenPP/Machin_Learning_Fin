import os
import csv
import math

test_result = open('./test-result','r')
#test_result = open('../../../output/34/test-result','r')
test = open('./test.csv','r')

labels= []
Open = []
close = []
high = []
date= []
low = []

for row in csv.DictReader(test_result, delimiter=' '):
	labels.append(float(row['labels']))
for row in csv.DictReader(test):
	Open.append(float(row['Open']))
	close.append(float(row['Close']))
	high.append(float(row['High']))
	date.append(row['Date'])
	low.append(float(row['Low']))


outputmoney=0
finialmoney=0


buymoney=0
sellmoney=0

walletmoney=0
savemoney=0
profit=0
total_profit = 0
number = 0

f=open('roi_big.csv','w')
f.write("date,callorput,open,high,close,buyprice,sellprice,profit,totalprofit,roi,outputmoney,walletmoney,number\n")


for i in range (0,len(labels),1):
	
	#walletmoney=walletmoney+sellmoney

	if(labels[i]==1):
		if(walletmoney<83000):
			outputmoney=outputmoney-(83000-walletmoney)
			walletmoney=walletmoney+(83000-walletmoney) 
		
		#number=1
		number=math.floor(walletmoney/83000)
		buymoney=number*83000
		walletmoney=walletmoney-buymoney
		if(low[i+5]+255<=Open[i+5]):
			sellmoney=number*(32000)
			sellprice=Open[i+5]-255
		else:
			sellmoney=(83000+(close[i+5]-Open[i+5]-1)*200)*number
			sellprice=close[i+5]
		profit=sellmoney-buymoney
		total_profit=total_profit+profit

		if(profit>0):
			walletmoney=walletmoney+buymoney+4*profit/4
			savemoney=savemoney+profit*0/4
		else:
			walletmoney=walletmoney+sellmoney
				

		finialmoney=walletmoney-(-outputmoney)+savemoney
		f.write(date[i+5]+',call,'+str(Open[i+5])+','+str(high[i+5])+','+str(close[i+5])+','+str(Open[i+5])+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
		print(date[i+5]+','+str(Open[i+5])+','+str(close[i+5])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))
		

	elif(labels[i]==-1):
		if(walletmoney<83000):
			outputmoney=outputmoney-(83000-walletmoney)
			walletmoney=walletmoney+(83000-walletmoney)
			
		#number=1
		number=math.floor(walletmoney/83000)
		buymoney=number*83000
		walletmoney=walletmoney-buymoney
		if(high[i+5]>=Open[i+5]+255):
			sellmoney=number*(32000)
			sellprice=Open[i+5]+255
		else:
			sellmoney=number*((Open[i+5]-close[i+5]-1)*200+83000)
			sellprice=close[i+5]
		if(sellmoney<=0):
			sellmoney=0
		profit=sellmoney-buymoney
		total_profit=total_profit+profit

		if(profit>0):
			walletmoney=walletmoney+buymoney+4*profit/4
			savemoney=savemoney+profit*0/4
		else:
			walletmoney=walletmoney+sellmoney
				

		finialmoney=walletmoney-(-outputmoney)+savemoney
		f.write(date[i+5]+',put,'+str(Open[i+5])+','+str(high[i+5])+','+str(close[i+5])+','+str(Open[i+5])+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
		print(date[i+5]+','+str(Open[i+5])+','+str(close[i+5])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))


f.close()
outputmoney=-outputmoney
print(finialmoney/outputmoney)
print "outputmoney =",outputmoney
print(total_profit)


