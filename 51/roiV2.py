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


outputmoney=0.0
finialmoney=0.0
buymoney=0.0
buyprice=0.0
sellmoney=0.0
buyday = 0
#walletmoney=0
walletmoney=0.0
savemoney=0.0
profit=0.0
total_profit = 0.0
number = 0
time = 0

buyornot = "no"
callorput = "call"

f=open('V2roi_big.csv','w')
f.write("date,callorput,open,high,close,buyprice,sellday,sellprice,profit,totalprofit,roi,outputmoney,walletmoney,number\n")



for i in range (0,len(labels),1):
	
	time += 1
	
	#walletmoney=walletmoney+sellmoney-buymoney
	
	if(buyornot=="yes" and callorput=="call"):
		if(0.05<=((high[i+10]-buyprice)/buyprice)):
			sellmoney=number*(83000+(buyprice*0.05-1)*200)
			sellprice=buyprice*1.05
			buyornot = "no"

			profit=sellmoney-buymoney
			total_profit=total_profit+profit

			if(profit>0):
				walletmoney=walletmoney+buymoney+profit*3/4
				savemoney=savemoney+profit*1/4
			else:
				walletmoney=walletmoney+sellmoney
						
			finialmoney=walletmoney-(-outputmoney)+savemoney
			f.write(date[buyday]+',call,'+str(Open[buyday])+','+str(high[buyday])+','+str(close[buyday])+','+str(Open[buyday])+','+date[i+10]+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
			print(date[buyday]+','+str(Open[buyday])+','+str(close[buyday])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))
			continue

		elif(0.03<=((buyprice-low[i+10])/buyprice)):
			sellmoney=number*(83000-(buyprice*0.03+1)*200)
			sellprice=buyprice*0.97
			buyornot = "no"

			profit=sellmoney-buymoney
			total_profit=total_profit+profit

			if(profit>0):
				walletmoney=walletmoney+buymoney+profit*3/4
				savemoney=savemoney+profit*1/4
			else:
				walletmoney=walletmoney+sellmoney
						

			finialmoney=walletmoney-(-outputmoney)+savemoney
			f.write(date[buyday]+',call,'+str(Open[buyday])+','+str(high[buyday])+','+str(close[buyday])+','+str(Open[buyday])+','+date[i+10]+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
			print(date[buyday]+','+str(Open[buyday])+','+str(close[buyday])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))
			continue

		elif(time==30):
			if(close[i+10]>=buyprice):
				sellmoney=number*(83000+(close[i+10]-buyprice-1)*200)
				sellprice=close[i+10]
				buyornot = "no"
				
				profit=sellmoney-buymoney
				total_profit=total_profit+profit

				if(profit>0):
					walletmoney=walletmoney+buymoney+profit*3/4
					savemoney=savemoney+profit*1/4
				else:
					walletmoney=walletmoney+sellmoney
						

				finialmoney=walletmoney-(-outputmoney)+savemoney
				f.write(date[buyday]+',call,'+str(Open[buyday])+','+str(high[buyday])+','+str(close[buyday])+','+str(Open[buyday])+','+date[i+10]+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
				print(date[buyday]+','+str(Open[buyday])+','+str(close[buyday])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))
				continue

			else:
				sellmoney=number*(83000-(buyprice-close[i+10]+1)*200)
				sellprice=close[i+10]
				buyornot = "no"

				profit=sellmoney-buymoney
				total_profit=total_profit+profit

				if(profit>0):
					walletmoney=walletmoney+buymoney+profit*3/4
					savemoney=savemoney+profit*1/4
				else:
					walletmoney=walletmoney+sellmoney
						

				finialmoney=walletmoney-(-outputmoney)+savemoney
				f.write(date[buyday]+',call,'+str(Open[buyday])+','+str(high[buyday])+','+str(close[buyday])+','+str(Open[buyday])+','+date[i+10]+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
				print(date[buyday]+','+str(Open[buyday])+','+str(close[buyday])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))
				continue

	if(buyornot=="yes" and callorput=="put"):
		if(0.05<=((buyprice-low[i+10])/buyprice)):
			sellmoney=number*(83000+(buyprice*0.05-1)*200)
			sellprice=buyprice*0.95
			buyornot = "no"

			profit=sellmoney-buymoney
			total_profit=total_profit+profit

			if(profit>0):
				walletmoney=walletmoney+buymoney+profit*3/4
				savemoney=savemoney+profit*1/4
			else:
				walletmoney=walletmoney+sellmoney
						
			finialmoney=walletmoney-(-outputmoney)+savemoney
			f.write(date[buyday]+',call,'+str(Open[buyday])+','+str(high[buyday])+','+str(close[buyday])+','+str(Open[buyday])+','+date[i+10]+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
			print(date[buyday]+','+str(Open[buyday])+','+str(close[buyday])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))
			continue

		elif(0.03<=((high[i+10]-buyprice)/buyprice)):
			sellmoney=number*(83000-(buyprice*0.03+1)*200)
			sellprice=buyprice*1.03
			buyornot = "no"

			profit=sellmoney-buymoney
			total_profit=total_profit+profit

			if(profit>0):
				walletmoney=walletmoney+buymoney+profit*3/4
				savemoney=savemoney+profit*1/4
			else:
				walletmoney=walletmoney+sellmoney
						

			finialmoney=walletmoney-(-outputmoney)+savemoney
			f.write(date[buyday]+',call,'+str(Open[buyday])+','+str(high[buyday])+','+str(close[buyday])+','+str(Open[buyday])+','+date[i+10]+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
			print(date[buyday]+','+str(Open[buyday])+','+str(close[buyday])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))
			continue

		elif(time==30):
			if(close[i+10]<=buyprice):
				sellmoney=number*(83000+(buyprice-close[i+10]-1)*200)
				sellprice=close[i+10]
				buyornot = "no"
				
				profit=sellmoney-buymoney
				total_profit=total_profit+profit

				if(profit>0):
					walletmoney=walletmoney+buymoney+profit*3/4
					savemoney=savemoney+profit*1/4
				else:
					walletmoney=walletmoney+sellmoney
						

				finialmoney=walletmoney-(-outputmoney)+savemoney
				f.write(date[buyday]+',call,'+str(Open[buyday])+','+str(high[buyday])+','+str(close[buyday])+','+str(Open[buyday])+','+date[i+10]+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
				print(date[buyday]+','+str(Open[buyday])+','+str(close[buyday])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))
				continue

			else:
				sellmoney=number*(83000-(close[i+10]-buyprice+1)*200)
				sellprice=close[i+10]
				buyornot = "no"

				profit=sellmoney-buymoney
				total_profit=total_profit+profit

				if(profit>0):
					walletmoney=walletmoney+buymoney+profit*3/4
					savemoney=savemoney+profit*1/4
				else:
					walletmoney=walletmoney+sellmoney
						

				finialmoney=walletmoney-(-outputmoney)+savemoney
				f.write(date[buyday]+',call,'+str(Open[buyday])+','+str(high[buyday])+','+str(close[buyday])+','+str(Open[buyday])+','+date[i+10]+','+str(sellprice)+','+str(profit)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(outputmoney)+','+str(walletmoney)+','+str(number)+'\n')
				print(date[buyday]+','+str(Open[buyday])+','+str(close[buyday])+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+','+str(number)+','+str(outputmoney))
				continue

	if(labels[i]==1 and buyornot=="no"):
		if(walletmoney<83000):
			outputmoney=outputmoney-(83000-walletmoney)
			walletmoney=walletmoney+(83000-walletmoney) 
		
		#number=1
		number=math.floor(walletmoney/83000)
		buymoney=number*83000
		buyday=i+10
		buyprice = Open[i+10]
		callorput="call"
		time=0
		buyornot="yes"

		walletmoney=walletmoney-buymoney

		
		

	elif(labels[i]==-1 and buyornot=="no"):
		if(walletmoney<83000):
			outputmoney=outputmoney-(83000-walletmoney)
			walletmoney=walletmoney+(83000-walletmoney)
			
		#number=1
		number=math.floor(walletmoney/83000)
		buymoney=number*83000
		buyday=i+10
		buyprice = Open[i+10]
		callorput="put"
		time=0
		buyornot="yes"

		walletmoney=walletmoney-buymoney
		


f.close()
outputmoney=-outputmoney
print(finialmoney/outputmoney)
print "outputmoney =",outputmoney
print(total_profit)