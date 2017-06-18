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

transation_Time = 1
allin = 1
save = 0
price_out = 1
StartDay = '2014/1/2'
EndDay = '2014/12/31'
##====	choose do Call or Put 1 is do 0 is not do 		====##
DoCall = 1
DoPut = 1


##      define function     ##
def CallorPutPrice(open_price,label):
	if(label == 1):
		if(open_price>=10000):
			x = open_price%200
			if(x>=100):
				y = open_price + (200-x) + (200*price_out)
				return y
			else:
				y = open_price - x + (200*price_out)
				return y
		else:
			x=open_price%100
			if(x>=50):
				y=open_price+(100-x) + (100*price_out)
				return y
			else:
				y=open_price-x + (100*price_out)
				return y
	elif(label == -1):
		if(open_price>=10000):
			x = open_price%200
			if(x>=100):
				y = open_price + (200-x) - (200*price_out)
				return y
			else:
				y = open_price - x - (200*price_out)
				return y
		else:
			x=open_price%100
			if(x>=50):
				y=open_price+(100-x) - (100*price_out)
				return y
			else:
				y=open_price-x - (100*price_out)
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
#my_txff = txff(train_data_feature_few_day)
my_txff = txff(0)
f=open('../../option_roi_result.csv','w')
f.write("date,roi\n")

buyfilelist = open('../../buyfilelist.csv','w')
buyfilelist.write("buy_or_sell,day,strike_price,number,id,PutorCall,buyprice,output_money,money_canbuy\n")

sellfilelist = open('../../sellfilelist.csv','w')
sellfilelist.write("buy_or_sell,sellday,id,number,buyday,buyprice,sellprice\n")

my_option = list(csv.DictReader(open('../../totaloption.csv','r')))

##==== 	Enter Train Test START and End Day ====##
StartDayi = 0
EndDayi = 0

for i in range(len(my_txff.open)):
	if(my_txff.date[i] == StartDay):
		StartDayi = i
	if(my_txff.date[i] == EndDay):
		EndDayi = i
print (StartDayi,EndDayi,EndDayi-StartDayi)
##====      start roi       ====##
which = 0
for i in range(0,(EndDayi-StartDayi)+1,1):
	##====      to count how many days      ====#
	for tra in iter(my_porfolio.transation_list):
		if(tra.haveorno == 1):
			tra.howmanyday += 1
	##====      if label != 0       ====##
	if(my_test_result.label[i] != 0):
		
		# strike_price is the price of call or put #
		strike_price = CallorPutPrice(my_txff.open[StartDayi+i],my_test_result.label[i])

		#   determine the dateline of option we buy     #
		date_after_month = datetime.datetime.strptime(my_txff.date[StartDayi+i], '%Y/%m/%d') + relativedelta(months=1)
		
		#  if 10 day is comming  start find the price in my_option   #
		for tra in iter(my_porfolio.transation_list):
			if(tra.howmanyday == transation_Time and tra.haveorno == 1):
				for row in my_option:
					if(my_txff.date[StartDayi+i]==row['date'] and tra.strike_price == float(row['strike_price']) and tra.callorput == row['callorput'] and tra.dateline == row['dateline']):
						if(tra.Take_Profit(float(row['high']))):
							my_porfolio.money_deposit += tra.number*(tra.sellprice-0.5)*save*50
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*allin*50
							tra.init_sell(row['date'])
							sellfilelist.write('sell'+','+str(tra.sellday)+','+str(tra.id)+','+str(tra.number)+','+str(tra.buyday)+','+str(tra.buyprice)+','+str(tra.sellprice)+'\n')
							break
						elif(tra.Stop_Loss(float(row['low']))):
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*50
							tra.init_sell(row['date'])
							sellfilelist.write('sell'+','+str(tra.sellday)+','+str(tra.id)+','+str(tra.number)+','+str(tra.buyday)+','+str(tra.buyprice)+','+str(tra.sellprice)+'\n')
							break
						my_porfolio.money_canbuy += tra.number*(float(row['close'])-0.5)*50
						tra.sellprice = float(row['close'])
						tra.init_sell(row['date'])
						sellfilelist.write('sell'+','+str(tra.sellday)+','+str(tra.id)+','+str(tra.number)+','+str(tra.buyday)+','+str(tra.buyprice)+','+str(tra.sellprice)+'\n')
						break


		for row in my_option:
			if(strike_price == float(row['strike_price']) and my_txff.date[StartDayi+i] == row['date'] and date_after_month.strftime("%Y%m")==row['dateline']):
				if(my_test_result.label[i] == 1 and row['callorput']=='call' and DoCall == 1):	
					if(my_porfolio.output_money <= 0):
						TheEed()				
					else:
						##====      get money from out_put to canbuy        ====##
						today_buyprice = float(row['open'])
						if(my_porfolio.money_canbuy <= (today_buyprice + 0.5)*50):
							my_porfolio.output_money -= ((today_buyprice + 0.5)*50 - my_porfolio.money_canbuy)
							my_porfolio.money_canbuy = (today_buyprice + 0.5)*50
						
						which = my_porfolio.WhichTransation()
						my_porfolio.transation_list[which].buy(today_buyprice,my_porfolio.money_canbuy,row['date'],float(row['strike_price']),row['callorput'],row['dateline'],my_test_result.call[i])
						my_porfolio.money_canbuy -= my_porfolio.transation_list[which].number*((today_buyprice+0.5)*50)
						print ('buy','transation_day = '+str(row['date']),'strike_price = '+str(row['strike_price']),'number = '+str(my_porfolio.transation_list[which].number),'id = '+str(my_porfolio.transation_list[which].id),'PutCall = '+str(row['callorput']),'buyprice = '+str(today_buyprice),'output_money = '+str(my_porfolio.output_money),'money_canbuy = '+str(my_porfolio.money_canbuy))
						buyfilelist.write('buy'+','+str(row['date'])+','+str(row['strike_price'])+','+str(my_porfolio.transation_list[which].number)+','+str(my_porfolio.transation_list[which].id)+','+str(row['callorput'])+','+str(today_buyprice)+','+str(my_porfolio.output_money)+','+str(my_porfolio.money_canbuy)+'\n')
						break
						
				elif(my_test_result.label[i] == -1 and row['callorput']=='put' and DoPut == 1):
					if(my_porfolio.output_money <= 0):
						TheEed()
						
					else:
						##====      get money from out_put to canbuy        ====##
						today_buyprice = float(row['open'])
						if(my_porfolio.money_canbuy <= ((today_buyprice+0.5)*50)):
							my_porfolio.output_money -= (((today_buyprice+0.5)*50) - my_porfolio.money_canbuy)
							my_porfolio.money_canbuy = ((today_buyprice+0.5)*50)
						
						which = my_porfolio.WhichTransation()

						my_porfolio.transation_list[which].buy(row['open'],my_porfolio.money_canbuy,row['date'],float(row['strike_price']),row['callorput'],row['dateline'],my_test_result.put[i])
						my_porfolio.money_canbuy -= my_porfolio.transation_list[which].number*((float(row['open'])+0.5)*50)
						print ('buy','transation_day = '+str(row['date']),'strike_price = '+str(row['strike_price']),'number = '+str(my_porfolio.transation_list[which].number),'id = '+str(my_porfolio.transation_list[which].id),'PutCall = '+str(row['callorput']),'buyprice = '+str(today_buyprice),'output_money = '+str(my_porfolio.output_money),'money_canbuy = '+str(my_porfolio.money_canbuy))
						buyfilelist.write('buy'+','+str(row['date'])+','+str(row['strike_price'])+','+str(my_porfolio.transation_list[which].number)+','+str(my_porfolio.transation_list[which].id)+','+str(row['callorput'])+','+str(today_buyprice)+','+str(my_porfolio.output_money)+','+str(my_porfolio.money_canbuy)+'\n')
						break
				# edit
		for tra in iter(my_porfolio.transation_list):
			if(tra.haveorno == 1):
				for row in my_option:
					if(my_txff.date[StartDayi+i]==row['date'] and tra.strike_price == float(row['strike_price']) and tra.callorput == row['callorput'] and tra.dateline == row['dateline']):
						if(tra.Take_Profit(float(row['high']))):
							my_porfolio.money_deposit += tra.number*(tra.sellprice-0.5)*save*50
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*allin*50
							tra.init_sell(row['date'])
							sellfilelist.write('sell'+','+str(tra.sellday)+','+str(tra.id)+','+str(tra.number)+','+str(tra.buyday)+','+str(tra.buyprice)+','+str(tra.sellprice)+'\n')
						elif(tra.Stop_Loss(float(row['low']))):
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*50
							tra.init_sell(row['date'])
							sellfilelist.write('sell'+','+str(tra.sellday)+','+str(tra.id)+','+str(tra.number)+','+str(tra.buyday)+','+str(tra.buyprice)+','+str(tra.sellprice)+'\n')
						break


	# if labels == 0
	else:
		#you need to check is the price ok
		for tra in iter(my_porfolio.transation_list):
			if(tra.haveorno == 1):
				for row in my_option:
					if(my_txff.date[StartDayi+i]==row['date'] and tra.strike_price == float(row['strike_price']) and tra.callorput == row['callorput'] and tra.dateline == row['dateline']):
						if(tra.Take_Profit(float(row['high']))):
							my_porfolio.money_deposit += tra.number*(tra.sellprice-0.5)*save*50
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*allin*50
							tra.init_sell(row['date'])
							sellfilelist.write('sell'+','+str(tra.sellday)+','+str(tra.id)+','+str(tra.number)+','+str(tra.buyday)+','+str(tra.buyprice)+','+str(tra.sellprice)+'\n')
						elif(tra.Stop_Loss(float(row['low']))):
							my_porfolio.money_canbuy += tra.number*(tra.sellprice-0.5)*50
							tra.init_sell(row['date'])
							sellfilelist.write('sell'+','+str(tra.sellday)+','+str(tra.id)+','+str(tra.number)+','+str(tra.buyday)+','+str(tra.buyprice)+','+str(tra.sellprice)+'\n')
						elif(tra.howmanyday == transation_Time):
							my_porfolio.money_canbuy += tra.number*(float(row['close'])-0.5)*50
							tra.sellprice = float(row['close'])
							tra.init_sell(row['date'])
							sellfilelist.write('sell'+','+str(tra.sellday)+','+str(tra.id)+','+str(tra.number)+','+str(tra.buyday)+','+str(tra.buyprice)+','+str(tra.sellprice)+'\n')
						break
	##==== start write the roi file  ====##
	f.write(str(my_txff.date[StartDayi+i])+','+str(ROI())+'\n')
	print (ROI())

TheEed()	