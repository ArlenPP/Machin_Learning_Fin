#====   for typing chinese  ====#
#!/usr/bin/python
# coding=utf8

import sys
import os
import csv
import math
import datetime
import codecs
import re
from dateutil.relativedelta import relativedelta
from option_class import porfolio
from option_class import transation
from option_class import test_result
from option_class import txff

##      set up porfolio condition       ##

transation_Time = 10
train_data_feature_few_day = 10
allin = 1
save = 0


##      define function     ##
def CallorPutPrice(open_price):
	if(open_price>=10000):
		x = open_price%200
		if(x>=100):
			y = open_price + (200-x)
			return y
		else:
			y = open_price - x
			return y
	else:
		x=open_price%100
		if(x>=50):
			y=open_price+(100-x)
			return y
		else:
			y=open_price-x
			return y
def ROI():
	tmp = 0
	for i in iter(my_porfolio.transation_list):
		if(i.haveorno == 1):
			tmp += i.number*i.buyprice*50
	roi = (tmp + my_porfolio.money_canbuy + my_porfolio.output_money + my_porfolio.money_deposit)/my_porfolio.total_output_money
	return roi

def TheEed():
	##====		!!!!problem!!!! 	====##	
	print ROI()
	sys.exit()

##      start code here         ##

my_porfolio = porfolio(transation_Time)
my_test_result = test_result()
my_txff = txff(train_data_feature_few_day)
f=open('option_roi_result.csv','w')
f.write("date,roi\n")

my_option = list(csv.DictReader(open('./totaloption.csv','r')))

##====      start roi       ====##
which = 0
for i in range(0,len(my_test_result.label),1):
	##====      to count how many days      ====#
	for tra in iter(my_porfolio.transation_list):
		if(tra.haveorno == 1):
			tra.howmanyday += 1
	##====      if label != 0       ====##
	if(my_test_result.label[i] != 0):
		
		# strike_price is the price of call or put #
		strike_price = CallorPutPrice(my_txff.open[i])

		#   determine the dateline of option we buy     #
		date_after_month = datetime.datetime.strptime(my_txff.date[i], '%Y/%m/%d') + relativedelta(months=1)
		
		#  if 10 day is comming  start find the price in my_option   #
		for tra in iter(my_porfolio.transation_list):
			if(tra.howmanyday == 10 and tra.haveorno == 1):
				for row in my_option:
					if(my_txff.date[i]==row['date'] and tra.strike_price == float(row['strike_price']) and tra.callorput == row['callorput'] and tra.dateline == row['dateline']):
						if(tra.Take_Profit(float(row['high']))):
							my_porfolio.money_deposit += tra.number*(tra.sellprice-0.5)*save*50
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*allin*50
							tra.init_sell(row['date'])
							break
						elif(tra.Stop_Loss(float(row['low']))):
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*50
							tra.init_sell(row['date'])
							break
						my_porfolio.money_canbuy += tra.number*(float(row['close'])-0.5)*50
						tra.init_sell(row['date'])
						break


		for row in my_option:
			if(strike_price == float(row['strike_price']) and my_txff.date[i] == row['date'] and date_after_month.strftime("%Y%m")==row['dateline']):
				if(my_test_result.label[i] == 1 and row['callorput']=='call'):	
					if(my_porfolio.output_money <= 0):
						TheEed()				
					else:
						##====      get money from out_put to canbuy        ====##
						today_buyprice = float(row['open'])
						if(my_porfolio.money_canbuy <= (today_buyprice + 0.5)*50):
							my_porfolio.output_money -= ((today_buyprice + 0.5)*50 - my_porfolio.money_canbuy)
							my_porfolio.money_canbuy = (today_buyprice + 0.5)*50
						
						which = my_porfolio.WhichTransation()

						my_porfolio.transation_list[which].buy(today_buyprice,my_porfolio.money_canbuy,row['date'],float(row['strike_price']),row['callorput'],row['dateline'])
						my_porfolio.money_canbuy -= my_porfolio.transation_list[which].number*((today_buyprice+0.5)*50)
						print ('buy','id=',my_porfolio.money_deposit,my_porfolio.transation_list[which].id,'PutCall=',row['callorput'],'output_money=',my_porfolio.output_money,'money_canbuy=',my_porfolio.money_canbuy,'transation_day=',row['date'],'strike_price=',row['strike_price'],'buyprice=',str(today_buyprice))
						break
						
				elif(my_test_result.label[i] == -1 and row['callorput']=='put'):
					if(my_porfolio.output_money <= 0):
						TheEed()
						
					else:
						##====      get money from out_put to canbuy        ====##
						if(my_porfolio.money_canbuy <= ((float(row['open'])+0.5)*50)):
							my_porfolio.output_money -= (((float(row['open'])+0.5)*50) - my_porfolio.money_canbuy)
							my_porfolio.money_canbuy = ((float(row['open'])+0.5)*50)
						
						which = my_porfolio.WhichTransation()

						my_porfolio.transation_list[which].buy(row['open'],my_porfolio.money_canbuy,row['date'],float(row['strike_price']),row['callorput'],row['dateline'])
						my_porfolio.money_canbuy -= my_porfolio.transation_list[which].number*((float(row['open'])+0.5)*50)
						print ('buy','id=',my_porfolio.money_deposit,my_porfolio.transation_list[which].id,'PutCall=',row['callorput'],'output_money=',my_porfolio.output_money,'money_canbuy=',my_porfolio.money_canbuy,'transation_day=',row['date'],'strike_price=',row['strike_price'],'buyprice=',row['open'])
						break
				# edit
		for tra in iter(my_porfolio.transation_list):
			if(tra.haveorno == 1):
				for row in my_option:
					if(my_txff.date[i]==row['date'] and tra.strike_price == float(row['strike_price']) and tra.callorput == row['callorput'] and tra.dateline == row['dateline']):
						if(tra.Take_Profit(float(row['high']))):
							my_porfolio.money_deposit += tra.number*(tra.sellprice-0.5)*save*50
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*allin*50
							tra.init_sell(row['date'])
						elif(tra.Stop_Loss(float(row['low']))):
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*50
							tra.init_sell(row['date'])
						break


	# if labels == 0
	else:
		#you need to check is the price ok
		for tra in iter(my_porfolio.transation_list):
			if(tra.haveorno == 1):
				for row in my_option:
					if(my_txff.date[i]==row['date'] and tra.strike_price == float(row['strike_price']) and tra.callorput == row['callorput'] and tra.dateline == row['dateline']):
						if(tra.Take_Profit(float(row['high']))):
							my_porfolio.money_deposit += tra.number*(tra.sellprice-0.5)*save*50
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*allin*50
							tra.init_sell(row['date'])
						elif(tra.Stop_Loss(float(row['low']))):
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*50
							tra.init_sell(row['date'])
						elif(tra.howmanyday == 10):
							my_porfolio.money_canbuy += tra.number*(float(row['close'])-0.5)*50
							tra.init_sell(row['date'])
						break
	##==== start write the roi file  ====##
	f.write(str(my_txff.date[i])+','+str(ROI())+'\n')
	print (ROI())

TheEed()	