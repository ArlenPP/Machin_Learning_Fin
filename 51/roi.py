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
#walletmoney=0
walletmoney=0
item = []
savemoney=0
profit=0
total_profit = 0
number = 0

f=open('roi_big.csv','w')
f.write("date,callorput,open,high,close,buyprice,sellprice,profit,totalprofit,roi,outputmoney,walletmoney,number\n")

for i in range (0,31,1):
	item.append(float(0.0))


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
		control = 1
		item[(i+10)%31]

		for x in range(i+11,i+41,1):
			if(0.05<=((high[x]-Open[i+10])/Open[i+10])):
				sellmoney=number*(83000+(Open[i+10]*0.05-1)*200)
				sellprice=Open[i+10]*1.05
				control = 0
				break
			elif(0.03<=((Open[i+10]-low[x])/Open[i+10])):
				sellmoney[x%31]=number*(83000-(Open[i+10]*0.03+1)*200)
				sellprice=Open[i+10]*0.97
				control = 0
				break
		
		if(control == 1):
			if(close[i+41]>=Open[i+10]):
				sellmoney=number*(83000+(close[i+41]-Open[i+10]-1)*200)
				sellprice=close[i+41]
			else:
				sellmoney=number*(83000-(Open[i+10]-close[i+41]+1)*200)
				sellprice=close[i+41]

		
		profit=sellmoney-buymoney
		total_profit=total_profit+profit

		if(profit>0):
			walletmoney=walletmoney+buymoney+profit*3/4
			savemoney=savemoney+profit*1/4
		else:
			walletmoney=walletmoney+sellmoney
				

		finialmoney=walletmoney-(-outputmoney)+savemoney
		f.write(date[i+10]+',call,'+str(Open[i+10])+','+str(high[i+10])+','+str(close[i+10])+','+str(Open[i+10])+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
		print(date[i+10]+','+str(Open[i+10])+','+str(close[i+10])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))
		

	elif(labels[i]==-1):
		if(walletmoney<83000):
			outputmoney=outputmoney-(83000-walletmoney)
			walletmoney=walletmoney+(83000-walletmoney)
			
		number=1
		#number=math.floor(walletmoney/83000)
		buymoney=number*83000
		walletmoney=walletmoney-buymoney
		control = 1
		for x in range(i+11,i+41,1):
			if(0.05<=((Open[i+10]-low[x])/Open[i+10])):
				sellmoney=number*(83000+(Open[i+10]*0.05-1)*200)
				sellprice=Open[i+10]*0.95
				control = 0
				break
			elif(0.03<=((high[x]-Open[i+10])/Open[i+10])):
				sellmoney=number*(83000-(Open[i+10]*0.03+1)*200)
				sellprice=Open[i+10]*1.03
				control = 0
				break
		
		if(control == 1):
			if(close[i+40]<=Open[i+10]):
				sellmoney=number*(83000+(Open[i+10]-close[i+40]-1)*200)
				sellprice=close[i+40]
			else:
				sellmoney=number*(83000-(close[i+40]-Open[i+10]+1)*200)
				sellprice=close[i+40]
		
		profit=sellmoney-buymoney
		total_profit=total_profit+profit

		if(profit>0):
			walletmoney=walletmoney+buymoney+profit*3/4
			savemoney=savemoney+profit*1/4
		else:
			walletmoney=walletmoney+sellmoney
				

		finialmoney=walletmoney-(-outputmoney)+savemoney
		f.write(date[i+10]+',put,'+str(Open[i+10])+','+str(high[i+10])+','+str(close[i+10])+','+str(Open[i+10])+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
		print(date[i+10]+','+str(Open[i+10])+','+str(close[i+10])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))


f.close()
outputmoney=-outputmoney
print(finialmoney/outputmoney)
print "outputmoney =",outputmoney
print(total_profit)


