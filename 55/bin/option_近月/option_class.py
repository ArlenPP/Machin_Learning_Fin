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
takeprofit = 3  #3.0 6w number ==4
stoploss = 0.85
init_output_money = 50000
init_money_canbuy = 50000
Max_Number = 200
##====	about odds 		====##
odd_allin_one = 1
odd_allin_two = 1
odd_allin_three = 1
##====	about money 	====##
money_allin_one = 1
money_allin_two = 0.7
money_allin_three = 0.5
##==== 	read file 		=====##
svm_result = csv.DictReader(open('../../test-result','r'),delimiter=' ')
txff_raw = csv.DictReader(open('../../1txff.csv','r'),delimiter=',')

##		class define		##

#==== define transation		====#
class transation:
	def HowManyNumber(self,money,price):
		return math.floor(money/((float(price)+0.5)*50))

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
		print ('sell','day = '+str(self.sellday),'id = '+ str(self.id),'sellprice = '+str(self.sellprice),'buyprice = '+str(self.buyprice),'number = '+str(self.number))

	def buy(self,buyprice,money_canbuy,buy_day,strike_price,callorput,dateline,odd):
		
		if(odd >= odd_allin_one):
			self.number = self.HowManyNumber(money_canbuy*money_allin_one,buyprice)
			if(self.number > Max_Number):
					self.number = Max_Number
		elif(odd_allin_one > odd >= odd_allin_two):
			if(self.HowManyNumber(money_canbuy*money_allin_two,buyprice) > 1):
				self.number = self.HowManyNumber(money_canbuy*money_allin_two,buyprice)
				if(self.number > Max_Number):
					self.number = Max_Number
			else:
				self.number = 1
		elif(odd_allin_two > odd >= odd_allin_three):
			if(self.HowManyNumber((money_canbuy*money_allin_three),buyprice) > 1):
				self.number = self.HowManyNumber(money_canbuy*money_allin_three,buyprice)
				if(self.number > Max_Number):
					self.number = Max_Number
			else:
				self.number = 1
		else:
			self.number = 1
	
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
		self.transation_list = [transation(i) for i in range(0,transation_T+1)]
	
	def WhichTransation(self):
		for tra in iter(self.transation_list):
			if(tra.haveorno == 0):
				return tra.id

#====	define test_result		====#
class test_result:
	def __init__(self):
		self.label = []
		self.call = []
		self.put = []
		for row in svm_result:
			self.label.append(int(row['labels']))
			self.call.append(float(row['1']))
			self.put.append(float(row['-1']))

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