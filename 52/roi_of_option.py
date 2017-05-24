#!/usr/bin/python
# coding=utf8

import os
import csv
import math
import datetime
import codecs
import re
from dateutil.relativedelta import relativedelta
'''
Note: this will requires python-dateutil. to install it you need to run in linux terminal.
>>sudo apt-get update && sudo apt-get install python-dateutil
'''


Labels= []
Open = []
Close = []
High = []
Low = []
Date = []

option_open = []
option_close = []
option_high = []
option_callorput = []
option_date = []
option_dateline = []
option_strike_price = []

test_result = open('./test-result','r')
#test_result = open('../../../output/33/test-result','r')
test = open('./test.csv','r')


#read history option 請將檔案放在同一個資料夾裡面的folder which name is "option" 

file_data = [] #list of option.csv filename
DATA_DIR = '../../History_Option/2017' #directory of option.csv


def natural_key(string_):
	"""See http://www.codinghorror.com/blog/archives/001018.html"""
	return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

for filename in os.listdir(DATA_DIR):
	if('.csv' in filename):
		file_data.append(filename)

file_data.sort(key=natural_key) #good initial sort but doesnt sort numerically very well so we need to use key: and f:

totaloption = open('./totaloption.csv','w')
totaloption.write("date,dateline,strike_price,callorput,open,high,close\n")

for filename in file_data:
	print(filename)

	tmp = codecs.open('../../History_Option/2017/'+filename,'r','big5')
	optionfile = tmp.read()


	file = codecs.open('./tmpfile.csv','w','utf8')
	file.write(optionfile)


	for row in csv.DictReader(open('./tmpfile.csv')):
		if row['契約'] == 'TXO':
			if (row['買賣權']=='買權'):
				x='call'
			else:
				x='put'
			totaloption.write(row['交易日期']+','+row['到期月份(週別)']+','+row['履約價']+','+x+','+row['開盤價']+','+row['最高價']+','+row['收盤價']+'\n')
totaloption.close()

#read history option and make totaloption 



''' read labels '''
for row in csv.DictReader(test_result,delimiter=' '):
	Labels.append(int(row['labels']))
test_result.close()

''' read test.csv '''
for row in csv.DictReader(test):
	Open.append(float(row['Open']))
	Date.append(row['Date'])
	Close.append(float(row['Close']))
	High.append(float(row['High']))
	Low.append(float(row['Low']))
test.close()





outputmoney=0
finialmoney=0

buymoney=0
sellmoney=0

number=0
walletmoney=0
savemoney=0
profit=0
total_profit=0
x=0
y=0

f=open('roi_result.csv','w')
f.write("date,callorput,dateline,strike_price,buyprice,big_open,sellprice,big_close,big_hight,big_low,total_profit,outputmoney,roi\n")

tmp = csv.DictReader(open('./totaloption.csv'))

#tmptotaloption = open('./totaloption.csv')
''' 計算 roi '''
for i in range(0,len(Labels),1):

	#y is call or put price
	x=Open[i+10]%100
	if(x>=50):
		y=Open[i+10]+(100-x)
	else:
		y=Open[i+10]-x
	#datatype is from string to datetime so we can add_month
	#add_month = 1 我們做近月交易(就是下個月) 如果要做遠月 調整 1
	date_after_month = datetime.datetime.strptime(Date[i+10], '%Y/%m/%d') + relativedelta(months=1)
	#datatype is from datetime back to string so we can compare with the dateline

	for row in tmp:
		if(Labels[i]==0):
			break
		if (y==float(row['strike_price']) and Date[i+10]==row['date'] and date_after_month.strftime("%Y%m")==row['dateline']):
			
			if(Labels[i]==1 and row['callorput']=='call'):
				if(float(row['open'])==0 or float(row['close'])==0):
					break
				if(walletmoney<float(row['open'])):
					outputmoney=outputmoney-(float(row['open'])-walletmoney)
					walletmoney=walletmoney+(float(row['open'])-walletmoney)

				#number=1
				number=math.floor(walletmoney/float(row['open']))
				buymoney=number*float(row['open'])
				walletmoney=walletmoney-buymoney
				if(float(row['high'])/float(row['open'])>=3):
					sellmoney=number*(float(row['open'])*3-1)
				else:
					sellmoney=number*(float(row['close'])-1)

				profit=sellmoney-buymoney
				total_profit=total_profit+profit

				#調整賺進來的錢要存下來多少
				
				if(profit>0):
					walletmoney=walletmoney+buymoney+4*profit/4
					savemoney=savemoney+profit*0/4
				else:
					walletmoney=walletmoney+sellmoney
				
				
				finialmoney=walletmoney-(-outputmoney)+savemoney
				f.write(row['date']+','+row['callorput']+','+row['dateline']+','+row['strike_price']+','+str(buymoney/number)+','+str(Open[i+10])+','+str(sellmoney/number)+','+str(Close[i+10])+','+str(High[i+10])+','+str(Low[i+10])+','+str(total_profit)+','+str(outputmoney)+','+str(-(finialmoney/outputmoney))+'\n')
				print(row['date'],row['callorput'],row['dateline'],row['strike_price'],buymoney/number,sellmoney/number,total_profit,outputmoney,-(finialmoney/outputmoney))
				break
				
			
			elif(Labels[i]==-1 and row['callorput']=='put'):
				if(float(row['open'])==0 or float(row['close'])==0):
					break
				if(walletmoney<float(row['open'])):
					outputmoney=outputmoney-(float(row['open'])-walletmoney)
					walletmoney=walletmoney+(float(row['open'])-walletmoney)

				#number=1
				number=math.floor(walletmoney/float(row['open']))
				buymoney=number*float(row['open'])
				walletmoney=walletmoney-buymoney
				if (float(row['high'])/float(row['open'])>=3):
					sellmoney=number*(float(row['open'])*3-1)
				else:
					sellmoney=number*(float(row['close'])-1)

				profit=sellmoney-buymoney
				total_profit=total_profit+profit

				#調整賺進來的錢要存下來多少
				
				if(profit>0):
					walletmoney=walletmoney+buymoney+4*profit/4
					savemoney=savemoney+profit*0/4
				else:
					walletmoney=walletmoney+sellmoney
				

				finialmoney=walletmoney-(-outputmoney)+savemoney
				f.write(row['date']+','+row['callorput']+','+row['dateline']+','+row['strike_price']+','+str(buymoney/number)+','+str(Open[i+10])+','+str(sellmoney/number)+','+str(Close[i+10])+','+str(High[i+10])+','+str(Low[i+10])+','+str(total_profit)+','+str(outputmoney)+','+str(-(finialmoney/outputmoney))+'\n')
				print(row['date'],row['callorput'],row['dateline'],row['strike_price'],buymoney/number,sellmoney/number,total_profit,outputmoney,-(finialmoney/outputmoney))
				break
			
f.close()
finialmoney=walletmoney-(-outputmoney)+savemoney
outputmoney=-outputmoney
print "roi =",finialmoney/outputmoney
print "outputmoney =",outputmoney
print "total_profit =",total_profit
