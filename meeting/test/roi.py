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

for row in csv.DictReader(test_result, delimiter=' '):
	labels.append(float(row['labels']))
for row in csv.DictReader(test):
	Open.append(float(row['Open']))
	close.append(float(row['Close']))
	high.append(float(row['High']))
	date.append(row['Date'])


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
f.write("date,callorput,open,high,close,buyprice,sellprice,totalprofit,roi\n")


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
		sellmoney=number*((close[i+5]-Open[i+5]-1)*200+83000)
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
		f.write(date[i+5]+',call,'+str(Open[i+5])+','+str(high[i+5])+','+str(close[i+5])+','+str(buymoney/number)+','+str(sellmoney/number)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+'\n')
		print("data\topen\tclose\ttotal_profit\troi\t")
		print(date[i+5]+','+str(Open[i+5])+','+str(close[i+5])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number))
		

	elif(labels[i]==-1):
		if(walletmoney<83000):
			outputmoney=outputmoney-(83000-walletmoney)
			walletmoney=walletmoney+(83000-walletmoney)
			
		#number=1
		number=math.floor(walletmoney/83000)
		buymoney=number*83000
		walletmoney=walletmoney-buymoney
		sellmoney=number*((Open[i+5]-close[i+5]-1)*200+83000)
		
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
		f.write(date[i+5]+',put,'+str(Open[i+5])+','+str(high[i+5])+','+str(close[i+5])+','+str(buymoney/number)+','+str(sellmoney/number)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+'\n')
		print("data\topen\tclose\ttotal_profit\troi\tnumber")
		print(date[i+5]+','+str(Open[i+5])+','+str(close[i+5])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number))


f.close()
outputmoney=-outputmoney
print(finialmoney/outputmoney)
print "outputmoney =",outputmoney
print(total_profit)


