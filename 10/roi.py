#today buy today sell

import os
import csv

test_result = open('../../../output/10/test-result','r')
test = open('./test.csv','r')

labels= []
open = []
close = []


for row in csv.DictReader(test_result, delimiter=' '):
	labels.append(float(row['labels']))


for row in csv.DictReader(test):
	open.append(float(row['Open']))
	close.append(float(row['Close']))

sumbuy=0
sumsell=0

for i in range (len(open)-len(labels),len(labels)-30,1):

	
	if(labels[i]==1):
		sumbuy=sumbuy+float(open[i])
		sumsell=sumsell+float(close[i+30])
	elif(labels[i]==-1):
		sumbuy=sumbuy+float(close[i+30])
		sumsell=sumsell+float(open[i])


print(sumsell/sumbuy)