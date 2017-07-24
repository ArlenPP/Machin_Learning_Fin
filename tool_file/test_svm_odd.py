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

##==== read file ====##
stock_right = csv.DictReader(open('./test_right_odd/right','r'),delimiter=' ')
svm_result = csv.DictReader(open('./test_right_odd/test-result','r'),delimiter=' ')


##==== append data ====##
class right:
	def __init__(self):
		self.label = []
		for row in stock_right:
			self.label.append(int(row['labels']))

class result:
	def __init__(self):
		self.label = []
		self.call = []
		self.put = []
		for row in svm_result:
			self.label.append(int(row['labels']))
			self.call.append(float(row['1']))
			self.put.append(float(row['-1']))

my_right = right()
my_result = result()

call_times = 0.0
call_right_times = 0.0
put_times = 0.0
put_right_times = 0.0
total = 0.0

get_call_right = 0.0
get_put_right = 0.0
get_total_call_right = 0.0
get_total_put_right = 0.0

for i in range(len(my_right.label)):
	if(my_result.label[i] == 1):
		call_times += 1
		total += 1
		if(my_result.label[i] == my_right.label[i]):
			call_right_times += 1
	elif(my_result.label[i] == -1):
		put_times += 1
		total += 1
		if(my_result.label[i] == my_right.label[i]):
			put_right_times += 1

	else:
		total += 1
		continue
for i in range(len(my_right.label)):
	if(my_right.label[i] == 1):
		get_total_call_right += 1
		if(my_result.label[i] == 1):
			get_call_right += 1
	elif(my_right.label[i] == -1):
		get_total_put_right += 1
		if(my_result.label[i] == -1):
			get_put_right += 1
	else:
		continue



print ("call_odd = "+str(float(call_right_times/call_times)))
print ("put_odd = "+str(float(put_right_times/put_times)))
print ("precision_TP(call_odd + put_odd) = "+str(float(call_right_times/call_times)+float(put_right_times/put_times)))
print (call_times,put_times,total)
print ('\n'+'get_call_right = '+str(get_call_right/get_total_call_right))
print ('get_put_right = '+str(get_put_right/get_total_put_right))
