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

svm_result_1 = csv.DictReader(open('./test-result_1','r'),delimiter=' ')
svm_result_2 = csv.DictReader(open('./test-result_2','r'),delimiter=' ')

class test_result_class:
	def __init__(self,result):
		self.label = []
		self.call = []
		self.put = []
		for row in result:
			self.label.append(int(row['labels']))
			#self.call.append(float(row['1']))
			#self.put.append(float(row['-1']))

test_result1 = test_result_class(svm_result_1)
test_result2 = test_result_class(svm_result_2)

f=open('./new_result','w')
f.write("labels 1 -1 0\n")

for i in range(len(test_result1.label)):
	if (test_result1.label[i] == test_result2.label[i] and test_result1.label[i] != '0'):
		f.write(str(test_result1.label[i])+' '+'0.5'+' 0.5 0\n')
	else:
		f.write('0 '+' 0.5'+' 0.5 0\n')