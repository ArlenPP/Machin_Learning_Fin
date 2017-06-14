#====	for typing chinese	====#
#!/usr/bin/python
# coding=utf8

import os
import csv
import math
import datetime
import codecs
import re
from dateutil.relativedelta import relativedelta

##		set up in and out condition		##
takeprofit = 2.5  #3.0 6w number ==4
stoploss = 0.8
init_output_money = 100000
init_money_canbuy = 0
max_allin_money = 45000
max_allin_number = 3
svm_result = csv.DictReader(open('./test-result','r'),delimiter=' ')
txff_raw = csv.DictReader(open('./txff.csv','r'),delimiter=',')

##		class define		##

#==== define transation		====#
class transation:
	def __init__(self,i):
		self.id = i
		self.buyday = "buyday"
		self.buyprice = 0.0
		self.number = 0
		self.callorput = 'none'
		self.strike_price = 0.0
		self.dateline = 0
		self.sellday = "sellday"
		self.sellprice = 0.0
		self.haveorno = 0
		self.howmanyday = 0
	def Take_Profit(self,today_high):
		if self.buyprice*takeprofit <= today_high:
			self.sellprice = self.buyprice*takeprofit
			return True
		else:
			return False
	def Stop_Loss(self,today_low):
		if self.buyprice*stoploss >= today_low:
			self.sellprice = self.buyprice*stoploss
			return True
		else:
			return False
	def init_sell(self,sellday):
		self.haveorno = 0
		self.howmanyday = 0
		self.sellday = sellday
		print ('sell',self.id,self.sellday,self.sellprice,self.buyprice)

	def buy(self,buyprice,money_canbuy,buy_day,strike_price,callorput,dateline):
		
		if(money_canbuy > max_allin_money and (float(buyprice)+0.5)*3 <= max_allin_money):
			self.number = max_allin_number
		else:
			self.number = math.floor(money_canbuy/((float(buyprice)+0.5)*50))
		
		#self.number = 1
		self.buyprice = (float(buyprice))
		self.buyday = buy_day
		self.haveorno = 1
		self.callorput = callorput
		self.dateline = dateline
		self.strike_price = strike_price

#====	define transation porfolio	====#
class porfolio:
	def __init__(self,transation_T):
		self.transation_period = transation_T
		self.total_output_money = init_output_money + init_money_canbuy
		self.output_money = init_output_money
		self.money_canbuy = init_money_canbuy
		self.money_deposit = 0.0
		#	append transation into transation_list
		self.transation_list = [transation(i) for i in range(0,transation_T)]
	
	def WhichTransation(self):
		for tra in iter(self.transation_list):
			if(tra.haveorno == 0):
				return tra.id

#====	define test_result		====#
class test_result:
	def __init__(self):
		self.label = [int(row['labels']) for row in svm_result]

#====	define txff		====#
class txff:
	def __init__(self,skip_day):
		self.open = []
		self.close =[]
		self.high = []
		self.low = []
		self.date = []
		#====		append data into list 		====#
		for row in txff_raw:
			self.open.append(float(row['Open']))
			self.close.append(float(row['Close']))
			self.high.append(float(row['High']))
			self.low.append(float(row['Low']))
			self.date.append(row['Date'])
		#====		erase train data feature few day 		====#
		self.date = self.date[skip_day:]
		self.open = self.open[skip_day:]
		self.close =self.close[skip_day:]
		self.high = self.high[skip_day:]
		self.low = self.low[skip_day:]



		
