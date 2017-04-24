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
		if(walletmoney<Open[i+10]):
			outputmoney=outputmoney-(Open[i+10]-walletmoney)
			walletmoney=walletmoney+(Open[i+10]-walletmoney) 
		
		#number=1
		number=math.floor(walletmoney/Open[i+10])
		buymoney=number*Open[i+10]
		walletmoney=walletmoney-buymoney
		sellmoney=number*close[i+10]
		
		profit=sellmoney-buymoney
		total_profit=total_profit+profit

		if(profit>0):
			walletmoney=walletmoney+buymoney+4*profit/4
			savemoney=savemoney+profit*0/4
		else:
			walletmoney=walletmoney+sellmoney
				

		finialmoney=walletmoney-(-outputmoney)+savemoney
		f.write(date[i+10]+',call,'+str(Open[i+10])+','+str(high[i+10])+','+str(close[i+10])+','+str(buymoney/number)+','+str(sellmoney/number)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+'\n')
		print(date[i+10]+','+str(Open[i+10])+','+str(high[i+10])+','+str(close[i+10])+','+str(buymoney/number)+','+str(sellmoney/number)+','+str(total_profit)+','+str(-(finialmoney/outputmoney)))
		

	elif(labels[i]==-1):
		if(walletmoney<Open[i+10]):
			outputmoney=outputmoney-(Open[i+10]-walletmoney)
			walletmoney=walletmoney+(Open[i+10]-walletmoney)
			
		#number=1
		number=math.floor(walletmoney/Open[i+10])
		buymoney=number*Open[i+10]
		walletmoney=walletmoney-buymoney
		sellmoney=number*(Open[i+10]+Open[i+10]-close[i+10])
		
		profit=sellmoney-buymoney
		total_profit=total_profit+profit

		if(profit>0):
			walletmoney=walletmoney+buymoney+4*profit/4
			savemoney=savemoney+profit*0/4
		else:
			walletmoney=walletmoney+sellmoney
				

		finialmoney=walletmoney-(-outputmoney)+savemoney
		f.write(date[i+10]+',put,'+str(Open[i+10])+','+str(high[i+10])+','+str(close[i+10])+','+str(buymoney/number)+','+str(sellmoney/number)+','+str(total_profit)+','+str(-(finialmoney/outputmoney))+'\n')
		print(date[i+10]+','+str(Open[i+10])+','+str(high[i+10])+','+str(close[i+10])+','+str(buymoney/number)+','+str(sellmoney/number)+','+str(total_profit)+','+str(-(finialmoney/outputmoney)))


f.close()
outputmoney=-outputmoney
print(finialmoney/outputmoney)
print "outputmoney =",outputmoney
print(total_profit)


