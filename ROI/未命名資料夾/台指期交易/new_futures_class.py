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
Max_Number = 200
##====	about odds 		====##
odd_allin_one = 0.8
odd_allin_two = 0.75
odd_allin_three = 0.5
##====	about money 	====##
money_allin_one = 1
money_allin_two = 0.7
money_allin_three = 0.5
##====	about transation	====##
futrues_margin = 83000
fee = 100
##==== 	read file 		=====##
svm_result = csv.DictReader(open('../../test-result','r'),delimiter=' ')
txff_raw = csv.DictReader(open('../../../Make_Train_Test_Data/database/1txff.csv','r'),delimiter=',')

##		class define		##

#====	define transation		====#
class transation:
	def HowManyNumber(self,money):
		return math.floor(money/((futrues_margin+fee)))

	def __init__(self,i):
		self.id = i
		self.buyday = "buyday"
		self.buyprice = 0.0
		self.number = 0
		self.callorput = 'none'
		self.dateline = 0
		self.sellday = "sellday"
		self.sellprice = 0.0
		self.haveorno = 0
		self.howmanyday = 0

#====	define profolio		====#
class profolio:
	def __init__(self,transation_T,init_money):
		self.transation_period = transation_T
		self.total_input_money = init_money
		self.transation_list = [transation(i) for i in range(0,transation_T)]



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
	def __init__(self):
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
